import tkinter as tk
from tkinter import ttk
import admin_addition
class admin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Welcome back admin")
        self.label = tk.Label(text="Home Page", font="comic")
        self.options = ["Home appliances", "Electronics", "Fashion", "Books", "sports"]
        self.selected_option = tk.StringVar()
        self.dropDown = ttk.Combobox(self.root, textvariable=self.selected_option, values=self.options)
        self.dropDown.pack(padx=15, pady=15)
        self.textbox = tk.Label(text="what would you like to do?")
        self.textbox.pack()
        self.button1 = tk.Button(self.root, text="add categories", command=self.add)
        self.button1.pack()
        self.button2 = tk.Button(self.root, text="update price", command=self.update)
        self.button2.pack()
        self.root.mainloop()


    def add(self):
        self.root.destroy()
        admin_addition.add(self.selected_option)
    def update(self):
        self.root.destroy()
