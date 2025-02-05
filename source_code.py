# ************************************************************************* 
# Program: source_code.py 
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN 
# Lecture / Lab Section: TC1L / TL3L 
# Trimester: 2430 
# Names: WESLEY_LIM_KHAI | CHEE_YEE_HONG | WONG_TIAN_YANG | LAU_CHIN_YANG 
# IDs: 242FC243FA | 242FC243L3 | 242FC2425U | 242FC2431H 
# Emails: wesleylimkopi@gmail.com | yeehongchee@gmail.com | WONG.TIAN.YANG@student.mmu.edu.my | jinyangliu00@gmail.com
# *************************************************************************
import json
import random
def load_user():
    try:
        with open("user.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    
def load_user_data(user_id):
    try:
        with open("data.json", "r") as f:
            datas = json.load(f)
            for data in datas:
                if data["User"] == user_id:
                    return data
            return []
    except FileNotFoundError:
        return []

def save_user_data(user_data):
    try:
        with open("data.json", "r") as f:
            datas = json.load(f)
    except FileNotFoundError:
        datas = []

    for i, data in enumerate(datas):
        if data["User"] == user_data["User"]:
            datas[i] = user_data
            break
    else:
        datas.append(user_data)

    with open("data.json", "w") as f:
        json.dump(datas, f, indent=4)
    
def save_user(users):
    with open("user.json", "w") as f:
        json.dump(users, f, indent=4)

def level_up(player):
    exp_needed = 100
    if player["Xp"] >= exp_needed:
        player["Xp"] -= exp_needed
        player["Level"] += 1
        player["Attack Power"] += 5
        player["Armor"] += 2
        player["Max Health"] += 20
        player["Health"] = player["Max Health"]
        print(f"\nCongratulations! You've leveled up to Level {player['Level']}!")
        print(f"New Stats -> Health: {player['Health']}/{player['Max Health']}, Attack Power: {player['Attack Power']}, Armor: {player['Armor']}")

def get_random_enemy(player):
    with open("enemy.json", "r") as f:
        enemy_data = json.load(f) 
    enemies = enemy_data["enemies"]       
    enemy = random.choice(enemies)
    print(enemy)
    scaled_enemy = enemy.copy()
    level_difference = player["Level"] - 1
    scaled_enemy["Level"] += level_difference
    scaled_enemy["Health"] += 15 * level_difference
    scaled_enemy["Attack Power"] += 5 * level_difference
    scaled_enemy["Armor"] += 3 * level_difference
    scaled_enemy["Xp Drop"] += 20 * level_difference
    scaled_enemy["Gold Drop"] += 5 * level_difference
    return scaled_enemy

def fight_enemy(player, enemy):
    print(f"\nYou encountered a {enemy["Name"]}!")
    while player["Health"] > 0 and enemy["Health"] > 0:
        print("\nChoose your attack:")
        print("1. Fire\n2. Ice\n3. Lightning")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            attack_type = "fire"
        elif choice == "2":
            attack_type = "ice"
        elif choice == "3":
            attack_type = "lightning"
        else:
            print("Invalid choice! You missed your turn.")
            attack_type = None

        if attack_type:
            damage = player["Attack Power"]
            if attack_type == enemy["Weakness"]:
                damage *= 2
                print("Critical hit!")
            enemy["Health"] -= max(0, damage - enemy["Armor"])
            print(f"You dealt {damage - enemy["Armor"]} damage. Enemy health: {enemy['Health']}")

        if enemy["Health"] > 0:
            damage = max(0, enemy["Attack Power"] - player["Armor"])
            player["Health"] -= damage
            print(f"The {enemy['Name']} attacked and dealt {damage} damage. Your health: {player['Health']}")

    if player["Health"] > 0:
        print(f"\nYou defeated the {enemy['Name']}!")
        player["Xp"] += enemy["Xp Drop"]
        player["Gold"] += enemy["Gold Drop"]
        print(f"Rewards: {enemy['Xp Drop']} EXP, {enemy['Gold Drop']} Gold")
        level_up(player)
        save_user_data(user_data)
    else:
        print("You have been defeated!")

def main():
    users = load_user()
    user_count = len(users) + 1
    login_count = 0

    while login_count == 0:

        login = int(input('1.Log In 2.Sign Up'))

        if login == 1:
            username = input("Enter username:")
            password = input("Enter password:")
            found = False
            for user in users:
                if user["Username"] == username and user["Password"] == password:
                    global user_id
                    #used to identify who's account data should be loaded
                    user_id = user["User"]
                    print(user_id)
                    login_count += 1
                    found = True
                    break
            if not found:
                print("Invalid username or password.")

            
        elif login == 2:
            username = input("Enter username:")
            password = input("Enter password:")
            user = {"User": user_count, "Username" : username, "Password" : password}
            user_id = user["User"]
            users.append(user)
            save_user(users) 
            login_count += 1
            

        else:
            print("Only enter 1 or 2")
main()

play = int(input("1. New game 2. Load game"))

if play == 1:
    level = 1
    hp = 100
    atk = 30
    armor = 10
    xp = 0
    gold = 100
    inventory_data = []
    combat_class = int(input("Choose your class: 1. Warrior 2. Archer 3. Mage"))

    if combat_class == 1:
        combat_type = "Warrior"

    elif combat_class == 2:
        combat_type = "Archer"

    elif combat_class == 3:
        combat_type = "Mage"

    else:
        print("Error, choose either 1, 2 or 3")

    user_data = {"User": user_id, "Class": combat_type, "Level": level, "Health": hp, "Max Health": hp, "Attack Power": atk, "Armor": armor, "Gold": gold, "Xp": xp, "Inventory": inventory_data}
    save_user_data(user_data)
    print(user_data)

elif play == 2:
    user_data = load_user_data(user_id)
    if user_data:
        print(user_data)
else:
    print("Only enter 1 or 2")
    
game_count = 1
while game_count == 1:
    game_choice = int(input("1. Fight monsters 2. Fight boss 3.Shop"))
    if game_choice == 1:
        fight_enemy(user_data, get_random_enemy(user_data))
    elif game_choice == 2:
        print("hi")

    elif game_choice == 3:
        print('hello')

    else:
        print("Only type 1, 2 or 3")
