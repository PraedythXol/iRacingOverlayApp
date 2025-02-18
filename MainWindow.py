import customtkinter
import tkinter as tk
from App import iRacingDisplay

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green") # Themes: blue (default), dark-blue, green

#base button class
class base_button(customtkinter.CTkButton):
    def __init__(self, root, text, function, row, column):
        self.button = customtkinter.CTkButton(root, text=text, command=function,
                                               text_color="white", font=("", 14, "bold"),
                                                 height=48, width=140, border_color="black", 
                                                 corner_radius=0, border_width=0, fg_color="#4c4c4c",
                                                 bg_color="#2b2b2b", hover_color="#d07c40")  #brighter hover #ff8934
        self.button.grid(row=row, column=column, pady=1, sticky="nwes")

#####create buttons from class
class home_button(base_button):
    def __init__(self,root):
        def go_home():
            return
        super().__init__(root, text="Home", function=go_home, row=0, column=0)
    
class telemetry_button(base_button):
    def __init__(self,root):
        def go_telemetry():
            return
        super().__init__(root, text="Input Telemetry", function=go_telemetry, row=1, column=0)

class relative_button(base_button):
    def __init__(self,root):
        def go_relative():
            return
        super().__init__(root, text="Relative", function=go_relative, row=2, column=0)

class standings_button(base_button):
    def __init__(self,root):
        def go_standings():
            return
        super().__init__(root, text="Standings", function=go_standings, row=3, column=0)

class trackmap_button(base_button):
    def __init__(self,root):
        def go_trackmap():
            return
        super().__init__(root, text="Track map", function=go_trackmap, row=4, column=0)

#base frame class
class base_frame(customtkinter.CTkFrame):
    def __init__(self,root, x, y, color, bordersize, row, column, sticky, columnspan, rowspan):
        self.frame = customtkinter.CTkFrame(root, width=x, height=y, fg_color=color, 
                                            bg_color=color, border_width=bordersize, 
                                            border_color="black", corner_radius=0)
        self.frame.grid(row=row, column=column, sticky=sticky, columnspan=columnspan, rowspan=rowspan)

##create frames from class
class contents_frame(base_frame):
    def __init__(self,root):
        super().__init__(root, x=140, y=720, color="#2b2b2b", bordersize=0, row=1, column=0, sticky="snew", columnspan=1, rowspan=9)
        
class title_frame(base_frame):
    def __init__(self,root):
        super().__init__(root, x=1000, y=80, color="#d07c40", bordersize=1, row=0, column=0, sticky="news", columnspan=10, rowspan=1)
        
class app_frame(base_frame):
    def __init__(self, root):
        super().__init__(root, x=860, y=720, color="#1d1d1d", bordersize=0, row=1, column=1, sticky="snew", columnspan=9, rowspan=9)

#Main app
class main_Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x800")
        self.root.minsize(1000,800)
        #self.root.maxsize(1000,800)
        self.root.title("Team Sora Racing Overlay")

        #creating frames
        self.app_frame = app_frame(root)
        self.contents_frame = contents_frame(root)
        self.title_frame = title_frame(root)
        
        #creating buttons
        self.home_button = home_button(self.contents_frame.frame)
        self.telemetry_button = telemetry_button(self.contents_frame.frame)
        self.relative_button = relative_button(self.contents_frame.frame)
        self.session_info_button = standings_button(self.contents_frame.frame)
        self.trackmap_button =  trackmap_button(self.contents_frame.frame)

        #stop frame resizing
        self.title_frame.frame.grid_propagate(False)
        self.app_frame.frame.grid_propagate(False)

        #title text
        self.title_text = customtkinter.CTkLabel(self.title_frame.frame, text="Official Team Sora Racing App", text_color="white", font=("", 42, "bold"))
        self.title_text.grid(row=0, column=0, sticky="es", pady=24, padx=300)

        def show_menu():
            return

        #menu text
        #self.menu_button = customtkinter.CTkButton(self.title_frame.frame, text="☰", text_color="white", font=("", 32, "bold"), command=show_menu, bg_color="#2b2b2b", fg_color="#2b2b2b", hover_color="#d07c40", corner_radius=20)
        #self.menu_button.grid(row=0, column=0, sticky="wsn", pady=0, padx=0)

        #switch and function to enable overlay position adjustment
        def switch_function():
            if self.switch_var.get() == "on":
                open_telemetry_window()
            else:
                close_telemetry_window()

        #creates telemetry_window overlay
        def open_telemetry_window():
            global input_telemetry
            input_telemetry = customtkinter.CTkToplevel()
            iRacingDisplay(input_telemetry)
            input_telemetry.wm_attributes("-topmost", 1)
            input_telemetry.overrideredirect(True)
            input_telemetry.mainloop()

        #closes the window
        def close_telemetry_window():
            input_telemetry.destroy()

        #create switch to control overlay set to off initially
        self.switch_var = customtkinter.StringVar(value='off')
        self.overlay_switch = customtkinter.CTkSwitch(root, command=switch_function, text="Show Overlay", 
                                                        bg_color="#2b2b2b", progress_color="#d07c40",
                                                        font=("",12,"bold"), variable=self.switch_var, onvalue="on", offvalue="off")
        self.overlay_switch.grid(row=9, column=0,sticky="wes", padx=10, pady=10)

        #quit button
        self.quit_button = customtkinter.CTkButton(root, height=6, width=40, text="X", 
                                                   command=quit, bg_color="#d07c40", fg_color="#d07c40", 
                                                   border_width=0, border_color="black", corner_radius=0, 
                                                   font=("Arial", 22, "bold"), hover_color="#ff964a", text_color="white")
        self.quit_button.grid(row=0, column=9, sticky="ne", pady=1, padx=1)

if __name__ == "__main__":
    root = customtkinter.CTk()
    main = main_Window(root)
    root.overrideredirect(True)
    root.mainloop()