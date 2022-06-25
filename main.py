import random


def guessgame():
    guess_count = 1
    guess = int(input("What is your guess number between 1 to 100? "))
    number = random.randint(1, 100)
    while guess != number:
        guess_count += 1
        if guess > number:
            print(f"You guessed a higher number. The number was:{number}")
            guess1 = input("Want to try to guess again? Enter Yes or no ")
            while guess1.lower() == "Yes":
                guess = int(input("What is your new guess number? "))
                '''if guess == number:
                    print("Hey!, You guessed the perfect number. The number was: ", number)
                    print(f"Congrats You got the right answer in {guess_count}")
                break'''
            if guess1.lower() == "No":
                print("You did well!")
            break
        elif guess < number:
            print("You guessed a lower number. The number was: ", number)
            while input("Want to try to guess again? Enter Yes or no ") == 'Yes':
                guess = int(input("What is your new guess number? "))
                '''if guess == number:
                    print("Hey!, You guessed the perfect number. The number was: ", number)
                    print(f"Congrats You got the right answer in {guess_count}")
                break'''
            while input("Want to try to guess again? Enter Yes or No ") == "No":
                print("You did well!")
    print("You got the perfect number", number)



guessgame()
