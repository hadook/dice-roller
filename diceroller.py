
class DiceRoller:
    """Base class that implements common attributes for the dice roller sub-classes"""

    operators = ['+', '-', '*', '/', 'd', 'kh', 'kl', 'cs']
    organizers = ['(', ')', '[', ']', ',']