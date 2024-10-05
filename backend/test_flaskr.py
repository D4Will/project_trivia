import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    @classmethod
    def setUpClass(self):
        """Define test variables and initialize app."""
        self.database_path = os.environ['TEST_DATABASE_PATH']
        self.app = create_app({
            'SQLALCHEMY_DATABASE_URI': self.database_path
        })
        self.client = self.app.test_client
        
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        response = self.client().get("/categories")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))
        
    def test_405_get_categories_with_post(self):
        response = self.client().post("/categories")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')
        self.assertEqual(data['error'], 405)

    def test_get_questions(self):
        response = self.client().get("/questions")
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(len(data['categories']))
        self.assertTrue(len(data['currentCategory']))
        
    def test_404_get_questions_does_not_exist(self):
        response = self.client().get("/questions?page=300")
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['error'], 404)
    
    def test_delete_question(self):
        response = self.client().delete("/questions/5")
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['deleted'])
        
    def test_404_delete_question_does_not_exist(self):
        response = self.client().delete("questions/1500")
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['error'], 404)
    
    def test_create_question(self):
        response = self.client().post("/questions", json={"question":"love?", "answer": "baby don't hurt me", "category": 1, "difficulty": 1})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['created'])
        new_id = data['created']
        
    def test_405_create_question_using_bad_endpoint(self):
        response = self.client().post("/questions/50", json={"question":"rock?", "answer": "paper", "category": 1, "difficulty": 1})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')
        self.assertEqual(data['error'], 405)
        
    def test_search_question(self):
        response = self.client().post("/search", json={"searchTerm":"what"})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['questions']), 8) #7
        self.assertEqual(data['totalQuestions'], 8)
        self.assertTrue(data['currentCategory'])
    
    def test_405_search_question_using_bad_endpoint(self):
        response = self.client().post("/questions/search", json={"searchTerm":"branch"})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['error'], 404)
        
    def test_get_questions_by_category(self):
        response = self.client().get("/categories/1/questions")
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['currentCategory'])
        
    def test_404_get_questions_by_nonexistent_category(self):
        response = self.client().get("/categories/7/questions")
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['error'], 404)
    
    def test_get_question_in_quiz(self):
        response = self.client().post("/quizzes", json={"quiz_category":"Geography", "previous_questions": [13]})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        
    def test_get_question_in_quiz(self):
        response = self.client().post("/quizzes", json={"quiz_category":"Geography", "previous_questions": [13]})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        
    def test_404_get_question_in_quiz_nonexistent_category(self):
        response = self.client().post("/quizzes", json={"quiz_category":"Animals", "previous_questions": [13]})
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['error'], 404)
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()