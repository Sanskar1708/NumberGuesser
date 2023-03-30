import random
chances = 1
n = random.randint(1, 100)
guess = int(input("Guess the computer's number: "))
numberOfGuess = 0
while chances < 10:
    x = 10 - chances
    chances = chances + 1
    numberOfGuess = numberOfGuess + 1
    if guess < n:
        print("That's low \n")
        print(f"Number of chances left {x} \n")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("That's high \n")
        print(f"Number of chances left {x} \n")
        guess = int(input("Enter number again: "))
    else:
        print("you guessed it right!! \n")
        print(f"It took you {numberOfGuess} times to guess the number")
        break