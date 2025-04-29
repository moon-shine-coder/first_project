from random import randint 

secret_number = randint(1, 100) 
attempts = 0 
main_attempts = 0 # Счётчик для попыток когда игрок угадывает число.
lst = [] #Список для хранения попыток пользователя.

while True:
    user_number = int(input())

    if user_number == secret_number:
        print("You're guess!")

        attempts += 1 
        lst.append(1)
        main_attempts += 1 #Обновление счётчика для попыток когда игрок угадывает число.

        if attempts == 0:
            print("\nAnd you guessed right on the first attempt. ")
        else:    
            print(f"\nThe number attempts is {attempts}.")
        
        if main_attempts >= 2: #Если пользователь захочет продолжить игру, то будет высчитано среднее колличесиво его попыток.
            average_of_attempts = round(sum(lst) / main_attempts, 1)
            print(f"\nThe average number of attempts is {average_of_attempts}.")

        answer= input("\nDo you wanna continue?('yes' or 'no') ")

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
        lst.append(1) 
    else:
        print("Your number is lower then guess number.")
        attempts += 1 
        lst.append(1)



