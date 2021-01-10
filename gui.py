import tkinter as tk
import slot as s
import prizes as p

from tkinter import messagebox as mb

class Gui:
    def __init__(self, master):
        super().__init__()
        self.master = master
        self._slot = s.slot()
        self._prize = p.prize()

        label_frame = tk.Frame(self.master)
        label_frame.pack()

        self.label_1 = tk.Label(label_frame, text="0")
        self.label_1.pack(side="left")
        
        self.label_2 = tk.Label(label_frame, text="0")
        self.label_2.pack(side="left")
        
        self.label_3 = tk.Label(label_frame, text="0")
        self.label_3.pack(side="right")

        button_frame = tk.Frame(self.master)
        button_frame.pack()

        self.button_bet = tk.Button(button_frame, text="bet", command=self.bet)
        self.button_bet.pack(side="left")

        self.button_play = tk.Button(button_frame, text="play", command=self.play)
        self.button_play.pack(side="right")

    def start(self):
        self.master.mainloop()

    # event handler for bets
    def bet(self):
        self._slot.bet()
        # disabled bet button after "coin" is inserted
        self.button_bet["state"] = tk.DISABLED
    
    # event handler for play
    def play(self):
        result = self._slot.play()
        if result is None:
            mb.showerror(message="You must bet to play", title="bet")
        else: 
            self.label_1["text"] = result[0]
            self.label_2["text"] = result[1]
            self.label_3["text"] = result[2]
            
            if result[0] == 7 and result[1] == 7 and result[2] == 7:
                mb.showinfo(message=f"You win the jackpot! \n $ {self._prize.big_prize()}", title="prize")
            elif result[0] == 7 and result[1] == 7 or result[0] == 7 and result[2] == 7 or result[1] == 7 and result[2] == 7:
                mb.showinfo(message=f"Doble 7, Double prize! \n $ {self._prize.double_prize()}", title="prize")
            elif result[0] == 7 or result[1] == 7 or result[2] == 7:
                mb.showinfo(message=f"You win a small prize \n $ {self._prize.small_prize()}", title="prize")

        # reactivate bet button for next play
        self.button_bet["state"] = tk.ACTIVE



            
  
if __name__ == "__main__":
    root = tk.Tk()
    gui = Gui(root)
    gui.start()