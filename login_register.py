
import tkinter as tk
import admin
import Homepage
import newaccount
import json
from tkinter import messagebox

class project_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("team #2 online shopping project")
        self.label = tk.Label(text="LOGIN PAGE", font="comic")
        self.label.pack(pady=50)
        self.label_email = tk.Label(text="Email")

        self.data = []
        self.loadData() 

        self.email = tk.StringVar()
        self.password = tk.StringVar()

        self.label_email.pack()
        self.entry = tk.Entry(self.root, textvariable=self.email)
        self.entry.pack()
        self.label_pass = tk.Label(text="password")
        self.label_pass.pack()

        self.entry1 = tk.Entry(self.root, textvariable=self.password)
        self.entry1.pack()
        self.login_button = tk.Button(self.root, text="login", command=self.admin_or_not)
        self.login_button.pack(pady=10)

        self.register_button = tk.Button(self.root, text="if you don't have account 'register' ", command=self.register)
        self.register_button.pack()
        self.root.mainloop()
    def admin_or_not(self):
        if self.email.get() == "admin@gmail.com" and self.password.get() == "admin123":
            self.root.destroy()
            admin.admin()
        else:
            for usr in self.data:
                if(usr["Email"]==self.email.get() and usr["Password"]==self.password.get()):
                    self.root.destroy()
                    Homepage.homepage(usr)
                    return
            messagebox.showerror("Error", "email or password may be wrong")

    def register(self):
        self.root.destroy()
        newaccount.new_account()
        
    def save(self):
        file = open("p3.json", "w")
        json.dump(self.data, file, indent=2)
        file.close()
    
    def loadData(self):
        try:
            file = open("p3.json")
            self.data = json.load(file)
            file.close()
            
        # to force to create file
        except FileNotFoundError:
            self.save()




project_GUI()
