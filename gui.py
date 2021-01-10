import tkinter as tk
import slot as s
import prizes as p

from tkinter import messagebox as mb
from PIL import Image, ImageTk

class Gui (tk.Frame):
    def __init__(self, master):
        # next line require for blink function
        tk.Frame.__init__(self, master)
        super().__init__()
        self.master = master
        self._slot = s.slot()
        self._prize = p.prize()
        
        jackpot_frame = tk.Frame(self.master)
        jackpot_frame.pack()
        
        self.label_jackpot = tk.Label(jackpot_frame, text=self._slot._get_jackpot())
        self.label_jackpot.pack(side="right")

        self.label_jackpot_text = tk.Label(jackpot_frame, text="JACKPOT", foreground="red")
        self.label_jackpot_text.pack(side="left")
        self.blink()

        label_frame = tk.Frame(self.master)
        label_frame.pack()

        self.button_bet = tk.Button(label_frame, text="BET", command=self.bet)
        self.button_bet.pack(side="left")

        self.label_1 = tk.Label(label_frame, text="0")
        self.label_1.pack(side="left")
        
        self.label_2 = tk.Label(label_frame, text="0")
        self.label_2.pack(side="left")
        
        self.label_3 = tk.Label(label_frame, text="0")
        self.label_3.pack(side="left")

        self.button_play = tk.Button(label_frame, text="PLAY", state="disabled", command=self.play)
        self.button_play.pack(side="right")

        image_frame = tk.Frame (self.master)
        image_frame.pack(side="bottom")

        self._image_file = Image.open("/home/rick/python/juegos/lucky7/src/images/main.png")
        self._image_file = self._image_file.resize((250,120))
        self._tkimage = ImageTk.PhotoImage(self._image_file)

        self.image = tk.Label(image=self._tkimage)
        self.image.pack(side="bottom")

    def start(self):
        self.master.mainloop()

    # event handler for bets
    def bet(self):
        self._slot.bet()
        # disabled bet button after "coin" is inserted
        self.button_bet["state"] = "disabled"
        # update jackpot value
        self.label_jackpot["text"] = self._slot._get_jackpot()
        # enable play button
        self.button_play["state"] = "active"
    
    # event handler for play
    def play(self):
        result = self._slot.play()
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
        self.button_bet["state"] = "active"
        # disable play button until next bet
        self.button_play["state"] = "disabled"
    
    def blink(self):
        # This function will blink the word JACKPOT 
        fg1 = "red"
        fg2 = "orange"
        if (self.label_jackpot_text.cget("foreground") == "red"):
            self.label_jackpot_text.configure(foreground=fg2)
        else:
            self.label_jackpot_text.configure(foreground=fg1)
        # this line actually blinks JACKPOT
        self.after(300, self.blink)

if __name__ == "__main__":
    root = tk.Tk()
    gui = Gui(root)
    gui.start()