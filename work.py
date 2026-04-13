from statistics import Statistics
from random import randint
from quiztaker import ask_question

def work(stats: Statistics):
    successful_work = ask_question()
    stats.money += randint(5, 15) if successful_work else 0
    print(f"You {'earned' if successful_work else 'did not earn'} money from work{'' if successful_work else 'because you failed the quiz'}. You now have {stats.money} money.")