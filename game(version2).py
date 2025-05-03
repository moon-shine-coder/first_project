from random import randint 

first, second =  map(int, input("Enter from which number to which number was the hidden number: ").split())
secret_number = randint(first, second) #Пользователь сам может выбирать диапазон чисел в котором будет генерироваться загаданное число.
print("What number did I make a wish for?")
attempts = 0 #Счётчик попыток за одит сеанс игры пользователя.
common_attempts = 0 #Счётчик общего числа попыток.
main_attempts = 0 # Счётчик попыток когда игрок угадывает число.


while True:
    try:
        user_number = int(input("I think it's the number: "))
    except ValueError:
        print("Enter numbers, not strings!")
    else:
        if user_number == secret_number:
            print("Yes, you're guess!")

            attempts += 1 #Обновление счётчика попыток за один сеанс игры пользователя.
            common_attempts += 1 #Обновление счётчика общих попыток.
            main_attempts += 1 #Обновление счётчика для попыток когда игрок угадывает число.

            if attempts == 1:
                print("\nAnd you guessed right on the first attempt.")
            else:    
                print(f"\nThe number attempts is {attempts}.")
            
            if main_attempts >= 2:
                response = input("Do you want to know your average number of attempts? ('yes' or 'no') ")
                if  response == "yes":
                    average_of_attempts = round(common_attempts / main_attempts, 1)
                    print(f"\nThe average number of attempts is {average_of_attempts}.")
                else:
                    print("\nok")

            answer= input("\nDo you wanna continue?('yes' or 'no') ")
            if answer == "yes":
                secret_number = randint(first, second)
                attempts = 0 
            else:
                break
        elif user_number > secret_number:
            print("No, your number is bigger then guess number.")
            attempts += 1
            common_attempts += 1 

        else:
            print("No, your number is lower then guess number.")
            attempts += 1 
            common_attempts += 1 
