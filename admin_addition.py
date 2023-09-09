import tkinter as tk
import categories
electronics = categories.Electronics()
e = electronics.Electronics_data
home_ap = categories.HomeAppliances()
h = home_ap.HomeAppliances_data
fashion = categories.Fashion()
f = fashion.Fashion_data

class add:
    def __init__(self, type):
        self.root = tk.Tk()
        self.root.title = "admin adds a category"
        self.root.geometry("500x500")
        self.label1 = tk.Label(text="name of item")
        self.label1.pack()
        self.name = tk.StringVar
        self.textbox = tk.Entry(self.root, textvariable = self.name)
        self.textbox.pack()
        self.label2 = tk.Label(text="brand")
        self.label2.pack()
        self.brand = tk.StringVar
        self.textbox2 = tk.Entry(self.root, textvariable= self.brand)
        self.textbox2.pack()
        self.label3 = tk.Label(text="model year")
        self.label3.pack()
        self.modelyear = tk.StringVar
        self.textbox3 = tk.Entry(self.root, textvariable=self.modelyear)
        self.textbox3.pack()
        self.button = tk.Button(text="click", command=prin)
        self.button.pack()
        self.new_item = {
            "name": self.name,
            "brand": self.brand,
            "model": self.modelyear
        }
        if type == "Electronics":
            e.append(self.new_item)
            print(e)
        elif type == "Home appliances":
            h.append(self.new_item)
            print(h)
        elif type == "Fashion":
            f.append(self.new_item)
            print(f)
        self.root.mainloop()
def prin():
    if type == "Electronics":
        print(e)
    elif type == "Home appliances":
        print(h)
    elif type == "Fashion":
        print(f)
