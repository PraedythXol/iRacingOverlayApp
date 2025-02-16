import irsdk
import tkinter as tk
from tkinter import ttk
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green") # Themes: blue (default), dark-blue, green

class iRacingDisplay:
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x125")
        self.root.title("iRacing Live Data")
        #root.configure(bg='#ff4b81')

        self.ir = irsdk.IRSDK()
        self.ir.startup()

        self.speed_label = customtkinter.CTkLabel(root, text="Speed: N/A", font=("Arial", 18), text_color="white")
        self.speed_label.place(relx=0.3, rely=0.28, anchor=CENTER)

        self.gear_label = customtkinter.CTkLabel(root, text="Gear: N/A", font=("Arial", 32), text_color="white")
        self.gear_label.place(relx=0.3,rely=0.6, anchor=CENTER)

        self.throttleprogress = DoubleVar()
        self.throttlebar = customtkinter.CTkProgressBar(root, orientation="vertical", variable=self.throttleprogress, height=100) 
        self.throttlebar.place(relx=0.6, rely=0.5, anchor=CENTER)
     
        self.brakeprogress = DoubleVar()
        self.brakebar = customtkinter.CTkProgressBar(root, orientation="vertical", variable=self.brakeprogress, height=100, progress_color="red"
                                                     , border_color="black") 
        self.brakebar.place(relx=0.70, rely=0.5, anchor=CENTER)

        self.update_values()

    def update_values(self):
        #get latest values from iracing
        if self.ir.is_connected:
            speed = self.ir['Speed']
            gear = self.ir['Gear']
            throttle = ((self.ir['Throttle']))
            brake = ((self.ir['Brake']))
            #value = self.brakebar.get()
            #print(value)

            #set speed
            if speed is not None:
                speed_kmh = speed * 3.6
                self.speed_label.configure(text=f"{speed_kmh:.0f}")
            #set gear
            if gear is not None:
                gear_text = 'R' if gear == -1 else 'N' if gear == 0 else str(gear)
                self.gear_label.configure(text=f"{gear_text}")
            #set throttle value
            if throttle is not None:
                if throttle == 1:
                    #create clean bars if value = 1
                    self.throttleprogress.set(0.99)
                    self.throttlebar.configure(fg_color='green')
                #create clean bars if value = 0
                elif throttle == 0:
                    self.throttleprogress.set(0)
                    self.throttlebar.configure(progress_color='#4a4d50')
                else:
                    self.throttleprogress.set(throttle)
                    self.throttlebar.configure(progress_color='green', fg_color='#4a4d50')
            #set brake value
            if brake is not None:
                if brake == 1:
                    #create clean bars if value = 1
                    self.brakeprogress.set(0.99)
                    self.brakebar.configure(fg_color='red')
                #create clean bars if value = 0
                elif brake == 0:
                    self.brakebar.set(0)
                    self.brakebar.configure(progress_color='#4a4d50')
                else:
                    self.brakebar.configure(progress_color='red', fg_color='#4a4d50')
                    self.brakeprogress.set(brake)
        #set base display
        else:
            self.speed_label.configure(text="000",font=("Arial", 12))
            self.gear_label.configure(text="N")
            self.root.quit()
        #update per 20ms
        self.root.after(20, self.update_values)

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = iRacingDisplay(root)
    root.wm_attributes("-topmost", 1)
    root.overrideredirect(True)
    root.mainloop()