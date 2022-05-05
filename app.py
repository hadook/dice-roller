import random

def execute(formula):
    if not formula.startswith('/roll'):
        print('invalid formula')
    else:
        print('executing')


print("\n--- Dice roller ---")

while True:
    formula = input('\n> ')
    execute(formula)
