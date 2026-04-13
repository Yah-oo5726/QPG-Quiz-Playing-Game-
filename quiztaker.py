from questions import MultipleChoiceQuestion, OpenEndedQuestion
from question_list import questions
from random import randint

def ask_question(test_question_index = None, test_answer = None):
    question = questions[randint(0, len(questions) - 1) if test_question_index is None else test_question_index]
    result = question.ask(test_answer=test_answer)
    if result:
        if test_answer is None:
            print("Correct!")
        return 1
    if test_answer is None:
        print("Incorrect!")
    return 0