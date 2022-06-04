

"""Base class that implements common attributes for the dice roller sub-classes"""
class DiceRoller:
    
    valid_tokens = [
        '+', '-', '*', '/',
        'd', 'kh', 'kl', 'cs',
        '=', '<', '>', '<=', '>=',
        '(', ')', '[', ']', ',' 
    ]

    # returns True if s is a valid token
    @classmethod
    def is_token(cls, s):
        return s.isdecimal() or (s in cls.valid_tokens)

