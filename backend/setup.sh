#!/bin/sh
export DATABASE_PATH='postgresql://postgres:abc@localhost:5432/trivia'
export TEST_DATABASE_PATH='postgresql://postgres:abc@localhost:5432/trivia_test'

export FLASK_DEBUG=True
export FLASK_APP=flaskr