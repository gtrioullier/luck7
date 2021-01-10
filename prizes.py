import slot as s

class prize:

    def __init__ (self):
        # 25 (coin) may be replaced by bet in future releases
        self._seven = 25 * 7
        self._double_seven = 25 * pow(7, 2)
        self._triple_seven = s.slot._get_jackpot(self)

    def small_prize (self):
        return self._seven
    
    def double_prize (self):
        return self._double_seven
    
    def big_prize (self):
        return self._triple_seven