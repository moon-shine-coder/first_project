from random import randint 

secret_number = randint(1, 100)
user_number = 0 
attempts = 0

while True:
    user_number = int(input())

    if user_number == secret_number:
        print("You're guess!")

        if attempts == 0:
            print("\nAnd you guessed right on the first try. ")
        else:    
            print(f"The numbers attempts is {attempts}")

        answer= input("Do you wanna continue?('yes' or 'no') ")

        if answer == "yes":
            secret_number = randint(1, 100)
            user_number = 0 
            attempts = 0
            continue
        else:
            break
    elif user_number > secret_number:
        print("Your number is bigger then guess number.")
        attempts += 1 
    else:
        print("Your number is lower then guess number.")
        attempts += 1 
        