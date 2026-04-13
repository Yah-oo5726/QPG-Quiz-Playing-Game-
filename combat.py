from quiztaker import ask_question
from statistics import Statistics
from random import randint

class Monster:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

def fight(stats: Statistics, monster: Monster):
    while stats.health > 0 and monster.health > 0:
        if ask_question():
            monster.health -= stats.attack
            if monster.health <= 0:
                stats.score += 100
                stats.level += 1
                print(f"You defeated the monster! Your score is now {stats.score} and you are combat level {stats.level}.")
                return True
            print(f"You hit the monster! It has {monster.health} health left.")
        else:
            print(f"You missed the monster! It has {monster.health} health left.")
        
        # Monster attacks back
        stats.health -= monster.attack
        if stats.health <= 0:
            print(f"You were defeated by the monster! Your score was {stats.score} and you reached combat level {stats.level}.")
            return False
        print(f"The monster hit you! You have {stats.health} health left.")

def combat(stats: Statistics):
    monster = Monster(health=stats.level * 5 + randint(-5, 5), attack=stats.level * 5 + randint(-5, 5))
    print(f"A wild monster appears! It has {monster.health} health and {monster.attack} attack.")
    return fight(stats, monster)