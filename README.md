# Trivia API
This project you to create questions based on categories so that you can quiz yourself and your friends with interesting facts.

Pre-requisites and Local Development

This app is being run on this project workspace which already has Python3, pip, and node installed which are needed to run the app.

## Backend

1. To install the dependencies for this project, cd into the backend using `cd backend`
    
   Once there install the dependencies from the requirements.txt file by running
   `pip3 install -r requirements.txt`

2. To set up the database, run the following:
```bash
createdb trivia
psql trivia < trivia.psql
```

3. Once the dependencies are installed, set up the local environment by running the following commands (you will want to update the database variables in setup.sh to match your own local postgreSQL environment):
```bash
    #Windows
    source env/Scripts/activate
    #otherwise
    source env/bin/activate
    
    source setup.sh
```
4. Enter the following into the terminal to start up the app:
    `flask run`
    
5. To run tests for the app. Open a new terminal and cd into the backend and run the following:
```bash
#Do not drop the database if this is your first time testing the app
dropdb bookshelf_test

createdb bookshelf_test
psql bookshelf_test < books.psql
python test_flaskr.py
```

Frontend

1. Open a new terminal and cd into the frontend with

    `cd frontend`
    
2. Once there run the following to install dependencies:

    `npm install`
    
3. Use the following to start the front end:

    `npm start`
    
API Documentation

Errors are returned as JSON objects and returned in the following format:
```bash
    {
        "success": False, 
        "error": 400,
        "message": "bad request"
    }
```

This API handles the following exceptions:
- 400 - bad request
- 404 - not found
- 405 - method not allowed
- 422 - unprocessable
- 500 - server error

Endpoints

GET /categories
* returns a list of categories
* sample request:
    
`curl http://127.0.0.1:5000/categories`
    
- sample response:
```bash
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "success": true
}
```
GET /questions

- returns all questions in pages of 10 and a list of categories
- sample request:
    
`curl http://127.0.0.1:5000/questions`
    
- sample response:
```bash
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "currentCategory": "Science", 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "totalQuestions": 19
}
```
DELETE /questions/id
- deletes a question by id
- sample request:
    
`curl http://127.0.0.1:5000/questions/14 -X DELETE`
    
- sample response:
```bash
{
  "deleted": 14, 
  "success": true
}
```
POST /questions
- creates a question
- sample request for creating:
    
```bash
curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Why?", "answer": "I know", "category": "1", "difficulty": "1"}'
```
    
- sample response:
```bash
{
  "created": 24, 
  "success": true
}
```
POST /search
- searches for a question
- sample request for searching:
```bash
curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"what"}'
```
- sample response:
```bash
{
  "currentCategory": "Sports", 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ], 
  "success": true, 
  "totalQuestions": 8
}
```
GET /categories/id/questions
- returns all questions for a specified category
- sample request:
    
`curl http://127.0.0.1:5000/categories/1/questions`
    
- sample response:
```bash   
{
  "currentCategory": "Sports", 
  "questions": [
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "I know", 
      "category": 1, 
      "difficulty": 1, 
      "id": 24, 
      "question": "Why?"
    }
  ], 
  "success": true, 
  "totalQuestions": 4
}
```
POST /quizzes
- returns the next quiz question
- sample request:
```bash
curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"quiz_category":"Sports", "previous_questions": "[22,24]"}'
```
- sample response
```bash
{
    "question": {
        "answer": "Tom Cruise",
        "category": 5,
        "difficulty": 4,
        "id": 4,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    "success": true
}
```