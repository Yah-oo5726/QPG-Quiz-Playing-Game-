from random import randrange
from statistics import Statistics

class Product:
    def __init__(self, price, type, effect_amount):
        self.price = price
        self.type = type
        self.effect_amount = effect_amount

def shop(stats: Statistics):
    products = [
        Product(price=randrange(10, 21), type="Health Potion", effect_amount=randrange(5, 11)),
        Product(price=randrange(10, 21), type="Damage Potion", effect_amount=randrange(3, 8)),
        Product(price=randrange(10, 21), type="Weapon", effect_amount=stats.level * 5 + randrange(-5, 5))
    ]
    print("Welcome to the shop! Here are the products available:")
    for i in range(len(products)):
        print(f"{i + 1}. {products[i].type} - Price: {products[i].price} coins, Strength: {products[i].effect_amount}")
    choice = int(input("Enter the number of the product you want to buy (or 0 to exit): "))
    if choice == 0:
        print("Exiting the shop.")
        return
    if products[choice - 1].price > stats.money:
        print("You don't have enough coins to buy that product. You leave the shop empty-handed.")
        return
    if products[choice - 1].type == "Health Potion":
        stats.health += products[choice - 1].effect_amount
        print(f"You bought a Health Potion and restored {products[choice - 1].effect_amount} health. Your current health is now {stats.health}.")
    elif products[choice - 1].type == "Damage Potion":
        stats.damage += products[choice - 1].effect_amount
        stats.attack = stats.damage + stats.damage_modifier
        print(f"You bought a Damage Potion and increased your damage by {products[choice - 1].effect_amount}. Your current attack is now {stats.attack}.")
    elif products[choice - 1].type == "Weapon":
        stats.damage_modifier += products[choice - 1].effect_amount
        stats.attack = stats.damage + stats.damage_modifier
        print(f"You bought a Weapon that increases your damage by {products[choice - 1].effect_amount}. Your current attack is now {stats.attack}.")
    return