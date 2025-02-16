import irsdk
import tkinter as tk
from tkinter import ttk
from tkinter import *


class iRacingDisplay:
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x125")
        self.root.title("iRacing Live Data")

        self.style = ttk.Style(root)
        self.style.theme_use('winnative')
        self.style.configure("red.Vertical.TProgressbar", foreground='red', background='red')
        self.style.configure("green.Vertical.TProgressbar", foreground='green', background='green')

        self.ir = irsdk.IRSDK()
        self.ir.startup()

        self.speed_label = ttk.Label(root, text="Speed: N/A", font=("Arial", 18))
        self.speed_label.place(relx=0.3, rely=0.28, anchor=CENTER)

        self.gear_label = ttk.Label(root, text="Gear: N/A", font=("Arial", 32))
        self.gear_label.place(relx=0.3,rely=0.6, anchor=CENTER)

        self.throttleprogress = IntVar()
        self.progressbar = ttk.Progressbar(root, orient=tk.VERTICAL, variable=self.throttleprogress, style="green.Vertical.TProgressbar")
        self.progressbar.place(relx=0.6, rely=0.5, anchor=CENTER)
     
        self.brakeprogress = IntVar()
        self.brakebar = ttk.Progressbar(root, orient=tk.VERTICAL, variable=self.brakeprogress, style="red.Vertical.TProgressbar")
        self.brakebar.place(relx=0.72, rely=0.5, anchor=CENTER)

        self.update_values()

    def update_values(self):
        if self.ir.is_connected:
            speed = self.ir['Speed']
            gear = self.ir['Gear']
            throttle = ((self.ir['Throttle']) * 100)
            brake = ((self.ir['Brake']) * 100)

            if speed is not None:
                speed_kmh = speed * 3.6
                self.speed_label.config(text=f"{speed_kmh:.0f}")
            
            if gear is not None:
                gear_text = 'R' if gear == -1 else 'N' if gear == 0 else str(gear)
                self.gear_label.config(text=f"{gear_text}")
            
            if throttle is not None:
                if throttle == 100:
                    self.throttleprogress.set(99.9)
                else:
                    self.throttleprogress.set(throttle)

            if brake is not None:
                if brake == 100:
                    self.brakeprogress.set(99.9)
                else:
                    self.brakeprogress.set(brake)
        else:
            self.speed_label.config(text="000",font=("Arial", 12))
            self.gear_label.config(text="N")
        
        self.root.after(20, self.update_values)

if __name__ == "__main__":
    root = tk.Tk()
    app = iRacingDisplay(root)
    #root.overrideredirect(True)
    root.mainloop()