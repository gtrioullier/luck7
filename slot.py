from random import randrange, seed
from os import path

class slot:
    """
    This class describes a slot machine
    It uses a binary file to hold jackpot
    """

# Initiator

    def __init__(self):
        self._coin = 25
        if not path.exists('jackpot.dat'):
            self._set_jackpot(0)
        self._bet = False

# Properties

    def _get_jackpot(self):
        with open ('jackpot.dat', 'rb') as f:
            pot_from_bytes = f.read()
            pot = int.from_bytes(pot_from_bytes, 'big', signed=False)
            return pot
    
    def _set_jackpot(self, pot):
        with open ('jackpot.dat', 'wb') as f:
            pot_to_bytes = pot.to_bytes(8, 'big', signed=False)
            f.write(pot_to_bytes)

# Private Methods

    def _number (self):
        """
        Private method to return a random integer between 0 and 9
        """
        seed()
        return randrange(10)

# Public Methods
    
    def bet(self):
        pot = self._get_jackpot() + self._coin
        self._set_jackpot(pot)
        self._bet = True

    def play (self):
        if self._bet:
            x = self._number()
            y = self._number()
            z = self._number()
            self._bet = False
            return 7, 7, z
        else:
            print('you must bet to play')