##finding missing numbers

""" NumberArr = [1,4,7,10,15]
def findMissingNumbers(x):
    numbers = set(x)
    numberLength = len(x)
    output=[]
    for i in range(1, x[-1]):
        if i not in numbers:
            output.append(i)
    return output
print(findMissingNumbers(NumberArr))
 """
# number guessing game - user should guess the number between two numbers and machine should help

from random import random, randrange, randint

firstNum = input('Choose first number: ')
firstNum = int(firstNum)
print(f'First number you have chosen is {firstNum}')
secondNum = int(input('Choose second number: '))
print(f'Second number you have chosen is {secondNum}')

rightNumberis = randint(firstNum, secondNum)
# print(f'Right number is {rightNumberis}')

guess = int(input('Your guess is: '))

if guess==rightNumberis:
    print(f'Correct! It is {guess}')
else:
    while guess!= rightNumberis:
        if guess>rightNumberis:
            print(f'{guess} is bigger than the number')
            guess=int(input('Retry guessing: '))
        else:
            print(f'{guess} is smaller than the number')
            guess=int(input('Retry guessing: '))
    print(f'Correct! It was {guess}. Congrats!')