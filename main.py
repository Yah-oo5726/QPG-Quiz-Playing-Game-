alive = True
from combat import combat
from statistics import Statistics
from shop import shop
from work import work

player = Statistics(health=30, level=1, money=0, damage=5, damage_modifier=0, score=0)
previous_choice = None

while alive:
    print("\nWhat would you like to do?")
    print("1. Work" if previous_choice != '1' else "(disabled, you just worked!)")
    print("2. Shop" if previous_choice != '2' else "(disabled, you just visited the shop!)")
    print("3. Combat" if previous_choice != '3' else "(disabled, you just fought a monster!)")
    print("4. Exit")
    choice = input("Enter the number of your choice: ")
    
    if choice == '1' and previous_choice != '1':
        work(player)
    elif choice == '2' and previous_choice != '2':
        shop(player)
    elif choice == '3' and previous_choice != '3':
        if not combat(player):
            alive = False
    elif choice == '4':
        print("Thanks for playing! Goodbye!")
        alive = False
    else:
        print("Invalid choice, please try again.")

    previous_choice = choice