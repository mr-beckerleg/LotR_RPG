import random
from time import sleep

def user_inputs():
    tries = int(input("Enter the number of tries you'd like available: "))
    sleep(1)
    start = int(input("Enter the LOW number for the game: "))
    sleep(1)
    stop = int(input("Enter the HIGH number for the game: "))
    sleep(1)
    game = int(input(f'''Would you like to use 
    
    1) User Input
    2) Linear Search
    3) Binary Search
    '''))

    if game == 1:
        guess_random_number(tries, start, stop)
    elif game == 2:
        guess_random_num_linear(tries, start, stop)
    else:
        guess_random_num_binary(tries, start, stop)     

def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    while tries != 0:
        print("Remaing tries:",tries)
        sleep(1)
        guess = int(input("Enter your guess: "))
        if guess < start or guess > stop:
            print("Choose a number between", start, "and", stop)
        else:
            if guess == target:
                sleep(1)
                print("\nNice Guess! You got it!\n")
                print(f"\nYou succeeded in {tries} tries!\n")
                return
            elif guess < target:
                sleep(1)
                print("\nToo Low\n")
            else:
                sleep(1)
                print("\nToo High\n")
            tries -= 1
    print("\nFAILED!\nThe correct number was", target)

def guess_random_num_linear(tries, start, stop):
    target = random.randint(start, stop)
    print(f'Target number: {target}')
    sleep(1)
    for x in range(start, stop +1):
        print(f"Program's Guess: {x}")
        sleep(1)
        if x == target:
            sleep(1)
            print("\nSuccess! The Program Guessed the Number!\n")
            return
        tries -= 1
        print("Remaing tries:",tries)
        if tries == 0:
            sleep(1)
            print("Program Failed!")
            return
    
def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop +1)
    print(f'''Random number to find: {target}!''')
    sleep(1)
    while tries != 0:
        guess =(start + stop) //2
        print(f"Program's Guess: {guess}")
        sleep(1)
        if guess == target:
            sleep(1)
            print("Success! The program guessed the Number!")
            print(f"\nThe program succeeded in {tries} tries. \n\nCan you beat that?\n")
            return
        elif guess < target:
            start = guess
            sleep(1)
            print("Guessing Higher!")
        else:
            stop = guess
            sleep(1)
            print("Guessing Lower!")
        tries -= 1
        print("Remaing tries:",tries)
        if tries == 1:
            guess = random.randint(start, stop)
    print("Program Failed!")
            
'''     Test Driver     '''
#guess_random_number(5, 0, 10)
#guess_random_num_linear(5, 0, 10)
#guess_random_num_binary(5, 0, 100)
user_inputs()
