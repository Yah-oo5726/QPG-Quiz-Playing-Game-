This is a project to help learn and remember facts. It might work, I don't know.



The game works like this:
Pick between work, shopping, and adventuring
Work -> gets money to shop
Shopping -> get supplies for adventuring
Adventuring -> Go slay monsters, increases score

Chase the high number!



To modify questions, edit question_list.py.
Your question_list.py should follow this template:

from questions import MultipleChoiceQuestion, OpenEndedQuestion

questions = [
    MultipleChoiceQuestion("What's the square root of 16?", 4, {"A": 2, "B": 4, "C": 8, "D": 64}),
    OpenEndedQuestion("What is the capital of France?", "Paris"),
]


To change starting stats, change the Statistics initialized in main.py