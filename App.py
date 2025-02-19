import irsdk
import tkinter as tk
from tkinter import ttk
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green") # Themes: blue (default), dark-blue, green

red = "#d34242"
blue= "#3b9dff"

class iRacingDisplay:
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x125")
        self.root.title("iRacing Live Data")
        self.root.configure(fg_color="#1d1d1d")
        #root.configure(bg='#ff4b81')

        
        def move_root(e):
            root.geometry(f'+{e.x_root-100}+{e.y_root-62.5}')

        self.root.bind("<B1-Motion>", move_root)

        self.ir = irsdk.IRSDK()
        self.ir.startup()

        #creating speed text
        self.speed_label = customtkinter.CTkLabel(root, text="Speed: N/A", font=("Bahnschrift", 24, "bold"), text_color="white")
        self.speed_label.place(relx=0.33, rely=0.28, anchor=CENTER)

        #creating gear text
        self.gear_label = customtkinter.CTkLabel(root, text="Gear: N/A", font=("Bahnschrift", 40, "bold"), text_color="#ff8934")
        self.gear_label.place(relx=0.33,rely=0.6, anchor=CENTER)

        #creating throttle bar
        self.throttleprogress = DoubleVar()
        self.throttlebar = customtkinter.CTkProgressBar(root, orientation="vertical", variable=self.throttleprogress, height=100, 
                                                        border_color="black", width=10) 
        self.throttlebar.place(relx=0.86, rely=0.5, anchor=CENTER)
     
        #creating brake bar
        self.brakeprogress = DoubleVar()
        self.brakebar = customtkinter.CTkProgressBar(root, orientation="vertical", variable=self.brakeprogress, height=100, progress_color=red
                                                     , border_color="black", width=10) 
        self.brakebar.place(relx=0.76, rely=0.5, anchor=CENTER)

        self.clutchprogress = DoubleVar()
        self.clutchbar = customtkinter.CTkProgressBar(root, orientation="vertical", variable=self.clutchprogress, height=100, progress_color=blue
                                                     , border_color="black", width=10) 
        self.clutchbar.place(relx=0.66, rely=0.5, anchor=CENTER)

        self.update_values()

    def update_values(self):
        #get latest values from iracing
        if self.ir.is_connected:
            speed = self.ir['Speed']
            gear = self.ir['Gear']
            throttle = ((self.ir['Throttle']))
            brake = ((self.ir['Brake']))
            clutch = ((self.ir['Clutch']))
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
                    self.brakebar.configure(fg_color=red)
                #create clean bars if value = 0
                elif brake == 0:
                    self.brakebar.set(0)
                    self.brakebar.configure(progress_color='#4a4d50')
                else:
                    self.brakebar.configure(progress_color=red, fg_color='#4a4d50')
                    self.brakeprogress.set(brake)

            if clutch is not None:
                if brake == 1:
                    #create clean bars if value = 1
                    self.clutchprogress.set(0.99)
                    self.clutchbar.configure(fg_color=blue)
                #create clean bars if value = 0
                elif clutch == 0:
                    self.clutchbar.set(0)
                    self.clutchbar.configure(progress_color='#4a4d50')
                else:
                    self.clutchbar.configure(progress_color=blue, fg_color='#4a4d50')
                    self.clutchprogress.set(clutch)
        #set base display
        else:
            self.speed_label.configure(text="000",font=("Bahnschrift", 24, "bold"))
            self.gear_label.configure(text="N", font=("Bahnschrift", 48, "bold"))
            #self.root.quit()
        #update per 20ms
        self.root.after(20, self.update_values)

#if __name__ == "__main__":
#    root = customtkinter.CTk()
#    app = iRacingDisplay(root)
#    root.wm_attributes("-topmost", 1)
#    root.overrideredirect(True)
#    root.mainloop()