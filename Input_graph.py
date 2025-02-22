import irsdk
import tkinter as tk
from tkinter import ttk
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green") # Themes: blue (default), dark-blue, green

class input_graph_overlay:
    def __init__(self,root):
        self.root = root
        self.root.geometry("400x125")
        self.root.title("iRacing Live Data")
        #self.root.configure(fg_color="#1d1d1d")


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = input_graph_overlay(root)
    root.wm_attributes("-topmost", 1)
    #root.overrideredirect(True)
    root.mainloop()
