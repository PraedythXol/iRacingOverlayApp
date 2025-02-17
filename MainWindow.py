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
                                                 height=56, width=140, border_color="black", 
                                                 corner_radius=0, border_width=0, fg_color="#d07c40",
                                                 bg_color="#2b2b2b", hover_color="#ff8934")
        self.button.grid(row=row, column=column, pady=0, sticky="nwes")

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
        super().__init__(root, text="Input Telemetry", function=go_telemetry, row=11, column=0)

class relative_button(base_button):
    def __init__(self,root):
        def go_relative():
            return
        super().__init__(root, text="Relative", function=go_relative, row=2, column=0)

class session_info_button(base_button):
    def __init__(self,root):
        def go_session_info():
            return
        super().__init__(root, text="Session Info", function=go_session_info, row=3, column=0)

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
        super().__init__(root, x=140, y=720, color="#2b2b2b", bordersize=0, row=9, column=0, sticky="snw",columnspan=14,rowspan=72)
        
class title_frame(base_frame):
    def __init__(self,root):
        super().__init__(root, x=1000, y=80, color="#d07c40", bordersize=0, row=0, column=0, sticky="n", columnspan=100, rowspan=8)

class app_frame(base_frame):
    def __init__(self, root):
        super().__init__(root, x=860, y=720, color="#242424", bordersize=0, row=9, column=15, sticky="sne", columnspan=86, rowspan=72)

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
        self.session_info_button = session_info_button(self.contents_frame.frame)
        self.trackmap_button =  trackmap_button(self.contents_frame.frame)

        #switch and function to enable overlay position adjustment
        def overlay_visibility():
            root = customtkinter.CTk()
            app = iRacingDisplay(root)
            root.wm_attributes("-topmost", 1)
            root.overrideredirect(True)
            root.mainloop()

        self.overlay_switch = customtkinter.CTkSwitch(root, command=overlay_visibility, text="Show Overlay", bg_color="#2b2b2b", progress_color="#d07c40")
        self.overlay_switch.grid(row=78, column=0,sticky="w", padx=10)

        #quit button
        #self.quit_button = customtkinter.CTkButton(root, height=6, width=40, text="X", 
        #                                           command=quit, bg_color="#d07c40", fg_color="#d07c40", 
        #                                           border_width=0, border_color="black", corner_radius=0, 
        #                                           font=("Arial", 22, "bold"), hover_color="#ff964a", text_color="white")
        #self.quit_button.grid(row=0, column=99, sticky="ne")

if __name__ == "__main__":
    root = customtkinter.CTk()
    main = main_Window(root)
    #root.overrideredirect(True)
    root.mainloop()