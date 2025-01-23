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
    global level
    global xp
    global gold
    global inventory_data
    level = 1
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

    user_data = {"User": user_id, "Class": combat_type, "Level": level, "Gold": gold, "Xp": xp, "Inventory": inventory_data}
    save_user_data(user_data)
    print(user_data)

elif play == 2:
    user_data = load_user_data(user_id)
    if user_data:
        print(user_data)
else:
    print("Only enter 1 or 2")
input()
