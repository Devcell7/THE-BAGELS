import random

def number():
    return random.randint(100,999)

def guess():
    guesss=0
    no=str(number())
    while guesss<10:
        guesss=guesss+1
        
        NO=str(input(f"Guess #{guesss}\n"))
        clues=[]
        if NO == no:
            print("you got the no")
            break
        for i in range(len(no)):
            if NO[i] == no[i]:
                 clues.append('Fermi')
            elif NO[i] in no:
                clues.append('Pico')
        if len(clues) == 0:
            print('Bagels')
        clues.sort()
        print(' '.join(clues))
    if guess == 10:
        print('Total guess are exceds')
    print(f'NO is {no}')


print("I am thinking of a 3-digit number. Try to guess what it is.")
print("The clues I give are...")
print('When I say:    That means:')
print(' Bagels        None of the digits is correct.')
print(' Pico          One digit is correct but in the wrong position.')
print(' Fermi         One digit is correct and in the right position.')
print('I have thought up a number. You have 10 guesses to get')
guess()