from questions import MultipleChoiceQuestion, OpenEndedQuestion
from unittest import TestCase
from quiztaker import ask_question

class TestQuestions(TestCase):
    def test_wrong_multiple_choice_answer(self):
        question = MultipleChoiceQuestion("What's the square root of 16?", 4, {"A": 2, "B": 4, "C": 8, "D": 64})
        self.assertFalse(question.ask(test_answer="A"))

    def test_correct_multiple_choice_answer(self):
        question = MultipleChoiceQuestion("What's the square root of 16?", 4, {"A": 2, "B": 4, "C": 8, "D": 64})
        self.assertTrue(question.ask(test_answer="B"))

    def test_lowercase_answer_multiple_choice_answer(self):
        question = MultipleChoiceQuestion("What's the square root of 16?", 4, {"A": 2, "B": 4, "C": 8, "D": 64})
        self.assertTrue(question.ask(test_answer="b"))

    def test_wrong_open_ended_answer(self):
        question = OpenEndedQuestion("What is the capital of France?", "Paris")
        self.assertFalse(question.ask(test_answer="London"))

    def test_correct_open_ended_answer(self):
        question = OpenEndedQuestion("What is the capital of France?", "Paris")
        self.assertTrue(question.ask(test_answer="Paris"))

    def test_lowercase_and_whitespace_answer_open_ended_answer(self):
        question = OpenEndedQuestion("What is the capital of France?", "Paris")
        self.assertTrue(question.ask(test_answer=" paris "))
    
    def test_uppercase_and_whitespace_answer_open_ended_answer(self):
        question = OpenEndedQuestion("What is the capital of France?", "Paris")
        self.assertTrue(question.ask(test_answer=" PARIS "))
    
    def test_mixedcase_and_whitespace_answer_open_ended_answer(self):
        question = OpenEndedQuestion("What is the capital of France?", "Paris")
        self.assertTrue(question.ask(test_answer=" PaRiS "))

    def test_quiztaker_wrong_answer(self):
        self.assertEqual(ask_question(test_question_index=0, test_answer="A"), 0)

    def test_quiztaker_right_answer(self):
        self.assertEqual(ask_question(test_question_index=0, test_answer="B"), 1)