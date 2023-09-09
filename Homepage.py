import tkinter as tk
from tkinter import ttk
import categories
import login_register
import cort
import search
class homepage:
    def __init__(self, usr):
        self.root = tk.Tk()
        self.root.title("Home Page")
        self.usr = usr
        self.name = self.usr["Username"]
        self.label = tk.Label(self.root, text=f"welcome, {self.name} choose from categories", font=("Arial", 15))
        self.label.pack(padx=30, pady=35)
        self.options = ["Home appliances", "Electronics", "Fashion", "Books", "Sports"]
        self.selected_option = tk.StringVar()
        self.dropDown = ttk.Combobox(self.root, textvariable=self.selected_option, values=self.options)
        self.dropDown.pack(padx=15, pady=15)
        self.button = tk.Button(self.root, text="ok", font=("Arial", 15), command=self.selected)
        self.button.pack(padx=15, pady=15)
        self.button2 = tk.Button(self.root, text="go back", font=("Arial",15), command=self.goBack)
        self.button2.place(x=0, y=0)
        self.button3 = tk.Button(self.root, text="show your cart", font=("Arial", 15), command=self.go_to_cart)
        self.button3.pack(padx=15, pady=15)
        self.search = tk.Button(self.root, text="search", command=self.searching)
        self.search.pack(padx=15, pady=15)
    def selected(self):
        if self.dropDown.get() == "Home appliances":
            self.root.destroy()
            categories.HomeAppliances()
            return
        elif self.dropDown.get() == "Electronics":
            self.root.destroy()
            categories.Electronics()
            return
        elif self.dropDown.get() == "Fashion":
            self.root.destroy()
            categories.Fashion()
            return
        elif self.dropDown.get() == "Books":
            self.root.destroy()
            categories.Books()
            return
        elif self.dropDown.get() == "Sports":
            self.root.destroy()
            categories.Sports()
            return
    def goBack(self):
        self.root.destroy()
        login_register.project_GUI()
        return
    def go_to_cart(self):
        self.root.destroy()
        cort.Cart()
    def searching(self):
        self.root.destroy()
        search.search()