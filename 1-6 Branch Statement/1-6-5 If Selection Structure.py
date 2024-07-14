# 2024-7-13 21:38 start, 2024-7-13 21:15 end  @YoCocoium If Selection Structure
import random


def guess_num_game():
    # Generate a random number between 1 and 100
    target_num = random.randint(1, 100)
    guess = None
    attempts = 0

    print('Guess your number between 1 and 100')
    while guess != target_num:
        try:
            guess = int(input("Please input your number: "))
            attempts += 1
            if guess < target_num:
                print("Your guess is too low")
            if guess > target_num:
                print("Your guess is too high")
            else:
                print(f"Your guess is correct,the number was {guess}")
                print(f"You guessed {attempts} times")
        except ValueError:
            print("Please enter a number,please try again")


# Start Game
guess_num_game()
