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
        self._min_jackpot = 1225
        self._path = "/home/rick/python/juegos/lucky7/src"
        if not path.exists(self._path + '/data/jackpot.dat'):
            self._set_jackpot(self._min_jackpot)
        elif (self._get_jackpot() < self._min_jackpot):
            self._set_jackpot(self._min_jackpot)
        if not path.exists(self._path + '/data/last_run.dat'):
            self._last_run = self._set_last_run(0, 0, 0)
        else:
            self._last_run = self._get_last_run()
        self._bet = False

# Properties

    def _get_jackpot(self):
        with open (self._path + '/data/jackpot.dat', 'rb') as f:
            pot_from_bytes = f.read()
            pot = int.from_bytes(pot_from_bytes, 'big', signed=False)
            return pot
    
    def _set_jackpot(self, pot):
        with open (self._path + '/data/jackpot.dat', 'wb') as f:
            pot_to_bytes = pot.to_bytes(8, 'big', signed=False)
            f.write(pot_to_bytes)
    
    def _get_last_run(self):
        with open (self._path + '/data/last_run.dat', 'rb') as f:
            list_number = []
            number_from_bytes = f.read(1)
            while number_from_bytes:
                number = int.from_bytes(number_from_bytes, 'big', signed=False)
                list_number.append(number)
                number_from_bytes = f.read(1)
            return tuple(list_number)
    
    def _set_last_run(self, x, y, z):
        numbers = [x, y, z]
        with open (self._path + '/data/last_run.dat', 'wb') as f:
            for number in numbers:
                number_to_bytes = number.to_bytes(1, 'big', signed=False)
                f.write(number_to_bytes)

# Private Methods

    def _number (self):
        """
        Private method to return a random integer between 0 and 9
        """
        seed()
        return randrange(10)
    
    def _check_min_jackpot(self, pot):
        """
        Private method to check minimun jackpot amount
        """
        if pot < self._min_jackpot:
            self._set_jackpot(self._min_jackpot)
        else:
            self._set_jackpot(pot)  
    
# Public Methods
    
    def bet(self):
        pot = self._get_jackpot() + self._coin
        self._check_min_jackpot(pot)
        self._bet = True

    def play (self):
        if self._bet:
            x = self._number()
            y = self._number()
            z = self._number()
            self._bet = False
            self._set_last_run(x, y, z)  
            return x, y, z
        else:
            print('you must bet to play')