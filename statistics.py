class Statistics:
    def __init__(self, health, level, money, damage, damage_modifier, score):
        self.health = health
        self.level = level
        self.money = money
        self.damage = damage
        self.damage_modifier = damage_modifier
        self.attack = damage + damage_modifier
        self.score = score