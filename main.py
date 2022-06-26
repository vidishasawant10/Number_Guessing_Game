import random


def guessgame():
    guess_count = 1
    guess = int(input("What is your guess number between 1 to 100? "))
    number = random.randint(1, 100)
    if guess > number:
        print(f"You guessed a higher number.")
        while guess != number:
            repeat = input("want to guess again enter yes or no")
            if repeat == "yes":
                guess_count += 1
                guess = int(input("What is your guess number between 1 to 100? "))
                if guess == number:
                    print(f"You got it right in {guess_count} counts. The number was {number}")
                elif guess > number:
                    print("You guess a higher number")
                elif guess < number:
                    print("You guess a lower number")
            elif repeat == 'no':
                print(f"You did well. Total count {guess_count}. The number was {number}")
                break

    elif guess < number:
        print("You guessed a lower number. The number was: ", number)
        while guess != number:
            repeat = input("want to guess again enter yes or no")
            if repeat == "yes":
                guess_count += 1
                guess = int(input("What is your guess number between 1 to 100? "))
                if guess == number:
                    print(f"You got it right in {guess_count} counts. The number was {number}")
                elif guess > number:
                    print("You guess a higher number")
                elif guess < number:
                    print("You guess a lower number")
            elif repeat == 'no':
                print(f"You did well. Total count {guess_count}. The number was {number}")
                break

    elif guess == number:
        print(f"You got the perfect number in {guess_count}. The number was {number}")


guessgame()
