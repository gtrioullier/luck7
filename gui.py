import tkinter as tk
import slot as s
import prizes as p
import tkinter.font as tkfont

from tkinter import messagebox as mb
from PIL import Image, ImageTk
from pygame import mixer as mx

class Gui (tk.Frame):
    def __init__(self, master):
        # next line require for blink function
        tk.Frame.__init__(self, master)
        mx.init(4100)
        self.master = master
        self._slot = s.slot()
        self._prize = p.prize()
        self._button_bg_active = "#fbff24"
        self._button_bg_disabled = "#f9fabb"
        self._openning_sound = mx.Sound("/home/rick/python/juegos/lucky7/src/sounds/slot2.wav")
        self._bet_sound = mx.Sound("/home/rick/python/juegos/lucky7/src/sounds/coin.wav")
        self._openning_sound.play()
        self._X, self._Y, self._Z = self._slot._get_last_run()


        # INFORMATION FRAME
        jackpot_frame = tk.Frame(self.master, borderwidth=0)
        jackpot_frame.place(x=0, y=0, height=30, width=250)

        self.label_jackpot_text = tk.Label(
            jackpot_frame,
            text="JACKPOT",
            fg="red",
            bg="#010747",
            font=tkfont.Font(family="arial", size=16, weight=tkfont.BOLD)
            )
        self.label_jackpot_text.place(x=0, y=0, height=30, width=125)
        self.blink()

        self.label_jackpot = tk.Label(
            jackpot_frame,
            text=f"$ {self._slot._get_jackpot()}",
            bg="#feffed",
            fg="red",
            font=tkfont.Font(family="arial", size=16, weight=tkfont.BOLD),
            borderwidth=2,
            relief="sunken"
            )
        self.label_jackpot.place(x=125, y=0, height=30, width=125)


        # GAME FRAME
        label_frame = tk.Frame(self.master, borderwidth=0)
        label_frame.place(x=0, y=30, height=80, width=250)

        self.button_bet = tk.Button(
            label_frame,
            text="BET",
            state="active",
            command=self.bet,
            activebackground=self._button_bg_active,
            background=self._button_bg_active,
            fg="black",
            font=tkfont.Font(weight=tkfont.BOLD),
            borderwidth=3,
            relief="raised"
            )
        self.button_bet.place(x=0, y=0, height=80, width=53)

        self.label_1 = tk.Label(
            label_frame,
            text=f"{self._X}",
            bg="#feffed",
            fg="black",
            font=tkfont.Font(underline=1, family="arial", size=30, weight=tkfont.BOLD),
            borderwidth=2,
            relief="groove"
            )
        self.label_1.place(x=53, y=0, height=80, width=48)
        
        self.label_2 = tk.Label(
            label_frame,
            text=f"{self._Y}",
            bg="#feffed",
            fg="black",
            font=tkfont.Font(underline=1, family="arial", size=30, weight=tkfont.BOLD),
            borderwidth=2,
            relief="groove"
            )
        self.label_2.place(x=101, y=0, height=80, width=48)
        
        self.label_3 = tk.Label(
            label_frame,
            text=f"{self._Z}",
            bg="#feffed",
            fg="black",
            font=tkfont.Font(underline=1, family="arial", size=30, weight=tkfont.BOLD),
            borderwidth=2,
            relief="groove"
            )
        self.label_3.place(x=149, y=0, height=80, width=48)

        self.button_play = tk.Button(
            label_frame,
            text="PLAY",
            state="disabled",
            command=self.play,
            bg=self._button_bg_disabled,
            fg="black",
            font=tkfont.Font(weight=tkfont.BOLD),
            borderwidth=3,
            relief="raised"
            )
        self.button_play.place(x=197, y=0, height=80, width=53)

        # IMAGE FRAME
        self._image_file = Image.open("/home/rick/python/juegos/lucky7/src/images/main.png")
        self._image_file = self._image_file.resize((250,120))
        self._tkimage = ImageTk.PhotoImage(self._image_file)

        self.image = tk.Label(image=self._tkimage)
        self.image.place(x=0, y=110, height=120, width=250)

    def start(self):
        self.master.mainloop()

    # event handler for bets
    def bet(self):
        # bet
        self._slot.bet()
        # play sound
        self._bet_sound.play()
        # disabled bet button after "coin" is inserted
        self.button_bet["state"] = "disabled"
        # update jackpot value
        self.label_jackpot["text"] = f"$ {self._slot._get_jackpot()}"
        # enable play button
        self.button_play["state"] = "active"
        # set buttons color according to state
        self.set_color()
    
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
        
        # update jackpot value
        self.label_jackpot["text"] = f"$ {self._slot._get_jackpot()}"
        # reactivate bet button for next play
        self.button_bet["state"] = "active"
        # disable play button until next bet
        self.button_play["state"] = "disabled"
        # set buttons color according to state
        self.set_color()
    
    def blink(self):
        # This function will blink the word JACKPOT 
        fg1 = "red"
        fg2 = "yellow"
        fg3 = "green"
        if (self.label_jackpot_text.cget("foreground") == fg1):
            self.label_jackpot_text.configure(foreground=fg2)
        elif (self.label_jackpot_text.cget("foreground") == fg2):
            self.label_jackpot_text.configure(foreground=fg3)
        else:
            self.label_jackpot_text.configure(foreground=fg1)
        # this line actually blinks JACKPOT
        self.after(300, self.blink)

    def set_color(self):
        # This function will set the colors of the button according to its state
        for button in [self.button_bet, self.button_play]:
            if (button.cget("state") == "disabled"):
                button.configure(bg=self._button_bg_disabled)
            else:
                button.configure(activebackground=self._button_bg_active)
                button.configure(background=self._button_bg_active)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("250x230")
    root.title("Luck 7")
    root.resizable(width=False, height=False)
    gui = Gui(root)
    gui.start()