from art import logo
import random
print(logo)
print("Welcome to the guessing game!")
num = random.randint(1, 100)

def easy():
    is_guessing = True
    attempts = 10
    print(f"You have {attempts} remaining to guess the number.")

    while is_guessing:
        guess = int(input("Make a guess: "))
        if guess != num and guess > num:
            attempts -= 1
            print("Too high, guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess != num and guess < num:
            attempts -= 1
            print("Too low, guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess != num:
            print("Please type a number")
        else:
            print(f"Congratulations, you guessed the number correctly! The number was: {num}")
            is_guessing = False
            break
        
        if attempts == 0:
            print(f"You ran out of attempts. Game over. The number was: {num}")
            is_guessing = False

def hard():
    is_guessing = True
    attempts = 5
    print(f"You have {attempts} remaining to guess the number.")

    while is_guessing:
        guess = int(input("Make a guess: "))
        if guess != num and guess > num:
            attempts -= 1
            print("Too high, guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess != num and guess < num:
            attempts -= 1
            print("Too low, guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess != num:
            print("Please type a number")
        else:
            print(f"Congratulations, you guessed the number correctly! The number was: {num}")
            is_guessing = False
            break
        
        if attempts == 0:
            print(f"You ran out of attempts. Game over. The number was: {num}")
            is_guessing = False



user_input = input("Choose a level of difficulty (hard/easy): ").lower()
if user_input == "easy":
    easy()
elif user_input == "hard":
    hard()
else:
    print("You didn't choose the appropriate answer. Goodbye!")
