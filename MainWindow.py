import customtkinter
import tkinter as tk
from App import telemetry_window_overlay
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green") # Themes: blue (default), dark-blue, green

#set text sizes
font_Small = ("Arial", 12, "bold")
font_Medium = ("Arial", 14, "bold")
font_Large = ("Arial", 18, "bold")
font_Extra_Large = ("Arial", 22, "bold")
font_Title = ("Arial", 42, "bold")

#set main colours
main_color_theme = "#d07c40"
main_color_theme_bright = "#ff8934"
main_light_color = "#4c4c4c"
main_contents_color = "#2b2b2b"
main_fg_color = "#1d1d1d"
transparent_color = "brown"

#main_contents_color = "#21222d"
#main_fg_color = "#171b23"


#base button class
class base_button(customtkinter.CTkButton):
    def __init__(self, root, text, function, row, column):
        self.button = customtkinter.CTkButton(root, text=text, command=function,
                                               text_color="white", font=font_Medium,
                                                 height=48, width=140, border_color="black", 
                                                 corner_radius=0, border_width=0, fg_color=main_contents_color,
                                                 bg_color=main_contents_color, hover_color=main_color_theme_bright)  
        self.button.grid(row=row, column=column, sticky="news")

#function to cycle between current "main frame", checks button number in array matches frame number in array
#moves the selected from onscreen and highlights the selected button 
#while moving all other frames off screen and changing their button color back to default
def move_main_frames(i):
    if len(main.main_buttons) == len(main.main_frames):
        for j in range(len(main.main_frames)):
            main.main_frames[j].grid(column=max_columnspan+1)
            main.main_buttons[j].configure(fg_color=main_contents_color)
            if i == j:
                main.main_frames[i].grid(column=1)
                main.main_buttons[i].configure(fg_color=main_color_theme)
    else: 
        print("Number of navigation buttons is not equal to number of navigable frames")
        root.destroy()

#####create buttons from class -- Navigation functions move selected frame to the screen and unselected ones off screen and highlight current frame
class home_button(base_button):
    def __init__(self,root):
        def go_home():
            i=0
            move_main_frames(i)
        super().__init__(root, text="Home", function=go_home, row=1, column=0)
    
class telemetry_button(base_button):
    def __init__(self,root):
        def go_telemetry():
            i=1
            move_main_frames(i)
        super().__init__(root, text="Input Telemetry", function=go_telemetry, row=2, column=0)

class relative_button(base_button):
    def __init__(self,root):
        def go_relative():
            i=2
            move_main_frames(i)
        super().__init__(root, text="Relative", function=go_relative, row=3, column=0)

class standings_button(base_button):
    def __init__(self,root):
        def go_standings():
            i=3
            move_main_frames(i)
        super().__init__(root, text="Standings", function=go_standings, row=4, column=0)

class trackmap_button(base_button):
    def __init__(self,root):
        def go_trackmap():
            i=4
            move_main_frames(i)
        super().__init__(root, text="Track map", function=go_trackmap, row=5, column=0)

#base frame class
class base_frame(customtkinter.CTkFrame):
    def __init__(self,root, x, y, color, bordersize, row, column, columnspan, rowspan):
        self.frame = customtkinter.CTkFrame(root, width=x, height=y, fg_color=color, 
                                            bg_color=color, border_width=bordersize, 
                                            border_color="black", corner_radius=0)
        self.frame.grid(row=row, column=column, sticky="nesw", columnspan=columnspan, rowspan=rowspan)

#total size of window grid
max_columnspan=20
max_rowspan=20

##create frames from class, most frames initialized at column 22 to be placed off-screen for later use
class contents_frame(base_frame):
    def __init__(self,root):
        super().__init__(root, x=140, y=720, color=main_contents_color, bordersize=0, row=2, column=0, columnspan=2, rowspan=18)
        
class title_frame(base_frame):
    def __init__(self,root):
        super().__init__(root, x=860, y=80, color=main_color_theme, bordersize=0, row=0, column=1, columnspan=18, rowspan=2)
        
class home_frame(base_frame):
    def __init__(self, root):
        super().__init__(root, x=860, y=720, color=main_fg_color, bordersize=0, row=2, column=1, columnspan=18, rowspan=18)

        #frame layout testing
        self.home_text = customtkinter.CTkLabel(self.frame, text="Welcome to Team Sora Racing", font=font_Large)
        self.home_text.grid(row=3, column=2, sticky="ew", padx=280, pady=50)
        self.settings_frame = customtkinter.CTkScrollableFrame(self.frame, height=554, width=780, fg_color=main_contents_color, scrollbar_button_color=main_color_theme, scrollbar_button_hover_color=main_color_theme_bright)
        self.settings_frame.grid(row=4, column=2, pady=0, padx=32)
        self.color_button = customtkinter.CTkButton(self.settings_frame, text="Change color", command=telemetry_color, fg_color=main_color_theme, hover_color=main_color_theme_bright, font=font_Medium)
        self.color_button.grid(row=4, column=2)

def telemetry_color():
            telemetry_window.gear_label.configure(text_color="white")

class input_telemetry_frame(base_frame):
    def __init__(self, root):
        super().__init__(root, x=860, y=720, color=main_fg_color, bordersize=0, row=2, column=22, columnspan=18, rowspan=18)

class relative_frame(base_frame):
    def __init__(self, root):
        super().__init__(root, x=860, y=720, color=main_fg_color, bordersize=0, row=2, column=22, columnspan=18, rowspan=18)

class standings_frame(base_frame):
    def __init__(self, root):
        super().__init__(root, x=860, y=720, color=main_fg_color, bordersize=0, row=2, column=22, columnspan=18, rowspan=18)

class trackmap_frame(base_frame):
    def __init__(self, root):
        super().__init__(root, x=860, y=720, color=main_fg_color, bordersize=0, row=2, column=22, columnspan=18, rowspan=18)

#Main app
class main_Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x800")
        #allows the use of "brown" to render frames transparent if required
        self.root.attributes("-transparentcolor", "brown")
        self.root.minsize(1000,800)
        #self.root.maxsize(1000,800)
        self.root.title("Team Sora Racing Overlay")

        #creating frames for title and menuing
        self.contents_frame = contents_frame(root)
        self.title_frame = title_frame(root)

        #creating frames to navigate through
        self.home_frame = home_frame(root)
        self.input_telemetry_frame = input_telemetry_frame(root)
        self.relative_frame = relative_frame(root)
        self.standings_frame = standings_frame(root)
        self.trackmap_frame = trackmap_frame(root)

        #creating buttons
        self.home_button = home_button(self.contents_frame.frame)
        self.telemetry_button = telemetry_button(self.contents_frame.frame)
        self.relative_button = relative_button(self.contents_frame.frame)
        self.standings_button = standings_button(self.contents_frame.frame)
        self.trackmap_button =  trackmap_button(self.contents_frame.frame)

        #array of main functionality frames/buttons
        #keep frames and buttons in order
        self.main_frames = [self.home_frame.frame, 
                            self.input_telemetry_frame.frame, 
                            self.relative_frame.frame, 
                            self.standings_frame.frame, 
                            self.trackmap_frame.frame]
        
        self.main_buttons = [self.home_button.button, 
                             self.telemetry_button.button, 
                             self.relative_button.button, 
                             self.standings_button.button, 
                             self.trackmap_button.button]

        #stop frame resizing to size of widgets in frame
        self.title_frame.frame.grid_propagate(False)
        for i in range(len(self.main_frames)):
            self.main_frames[i].grid_propagate(False)

        #title text
        self.title_text = customtkinter.CTkLabel(self.title_frame.frame, text="Official Team Sora Racing App", text_color="white", font=font_Title)
        self.title_text.grid(row=0, column=1, sticky="es", pady=24, padx=220)

        #set home page button as active
        self.main_buttons[0].configure(fg_color=main_color_theme)

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
            global telemetry_window
            telemetry_window = telemetry_window_overlay(input_telemetry)
            input_telemetry.wm_attributes("-topmost", 1)
            input_telemetry.overrideredirect(True)
            input_telemetry.mainloop()

        #closes the telemetry_window
        def close_telemetry_window():
            input_telemetry.destroy()

        #create switch to control overlay, set to off initially
        self.switch_var = customtkinter.StringVar(value='off')
        self.overlay_switch = customtkinter.CTkSwitch(root, command=switch_function, text="Show Overlay", 
                                                        bg_color=main_contents_color, progress_color=main_color_theme,
                                                        font=font_Small, variable=self.switch_var, onvalue="on", offvalue="off")
        self.overlay_switch.grid(row=19, column=0,sticky="wes", padx=10, pady=10)

if __name__ == "__main__":
    root = customtkinter.CTk()
    main = main_Window(root)
    #root.overrideredirect(True)
    root.mainloop()