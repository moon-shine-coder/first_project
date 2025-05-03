from random import randint 

secret_number = randint(1, 100)
user_number = 0

while secret_number != user_number:
    user_number = int(input())
    if user_number == secret_number:
        print("You're guess!")
    elif user_number > secret_number:
        print("Your number is bigger then guess number.")
    else:
        print("Your number is lower then guess number.")
print(" ")
        