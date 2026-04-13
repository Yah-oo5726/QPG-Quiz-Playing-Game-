This is a project to help learn and remember facts. It might work, I don't know.



The game works like this:
Pick between work, shopping, and adventuring
Work -> gets money to shop
Shopping -> get supplies for adventuring
Adventuring -> Go slay monsters, increases score

Chase the high number!



To modify questions, edit question_list.py.
Some tests might fail after you change this. This doesn't matter; the tests are mainly for development purposes.

You do have to make your own question_list.py.
The template the tests assume exists is:


from questions import MultipleChoiceQuestion, OpenEndedQuestion

questions = [
    MultipleChoiceQuestion("What's the square root of 16?", 4, {"A": 2, "B": 4, "C": 8, "D": 64}),
    OpenEndedQuestion("What is the capital of France?", "Paris"),
]


Your question_list.py should also follow this template