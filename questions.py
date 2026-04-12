from enum import Enum

class QuestionType(Enum):
    MULTIPLE_CHOICE = 0
    OPEN_ENDED = 1

class Question:
    def __init__(self, text, answer, question_type):
        self.text = text
        self.answer = answer
        self.question_type = question_type

    def ask(self, test_answer=None):
        raise NotImplementedError("Subclasses must implement this method")

class MultipleChoiceQuestion(Question):
    def __init__(self, text, answer, options):
        #note: answer should be the value of the correct option, not the key
        super().__init__(text, answer, QuestionType.MULTIPLE_CHOICE)
        self.options = options
    
    def ask(self, test_answer=None):
        answer = None
        if test_answer is None:
            print(self.text + " Multiple Choice")
            for key, value in self.options.items():
                print(f"{key}: {value}")
            answer = input("Your answer: ")
        else:
            answer = test_answer
        if answer.strip().upper() not in self.options:
            return False
        answer = self.options[answer.strip().upper()]
        return answer == self.answer


class OpenEndedQuestion(Question):
    def __init__(self, text, answer):
        super().__init__(text, answer, QuestionType.OPEN_ENDED)
    
    def ask(self, test_answer=None):
        answer = None
        if test_answer is None:
            print(self.text + " Open Ended")
            answer = input("Your answer: ")
        else:
            answer = test_answer
        answer = answer.strip().lower()
        return answer == self.answer.strip().lower()

questions = [
    MultipleChoiceQuestion("What's the square root of 16?", 4, {"A": 2, "B": 4, "C": 8, "D": 64}),
    OpenEndedQuestion("What is the capital of France?", "Paris"),
]