import random

random_number = int(random.random() * 10)
tries = 3
user_input = int(input("Enter the number: "))

def gameWin(user_score):
    print(f"Congratulations! You have guessed the number and scored {user_score} points.")


for i in range(tries):
    if user_input == random_number and tries == 3:
        gameWin(100)
        break
    elif user_input == random_number and tries == 2:
        gameWin(66)
        break
    elif user_input == random_number and tries == 1:
        gameWin(33)
        break
    else:
        tries = tries - 1
        if tries > 0:
            print("Wrong guess.")
            user_input = int(input("Enter the number again: "))
        else:
            print("Game Over!")