import slot as s

class prize:

    def __init__ (self):
        # 25 (coin) may be replaced by bet in future releases
        self._seven = 25 * 7
        self._double_seven = 25 * pow(7, 2)

    def small_prize (self):
        s.slot()._set_jackpot(s.slot()._get_jackpot() - self._seven)
        return self._seven
    
    def double_prize (self):
        s.slot()._set_jackpot(s.slot()._get_jackpot() - self._double_seven)
        return self._double_seven

    def big_prize (self):
        return s.slot()._get_jackpot()