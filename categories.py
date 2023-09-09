import tkinter as tk
import cort
class HomeAppliances:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("HomeAppliances")
        self.show_button = tk.Button(self.root,text="show items", font=("Arial", 15), command=self.HomeAppliances_data_list)
        self.show_button.pack(padx=15, pady=15)
        self.HomeAppliances_data = [
            {
             "name": "washing machine",
             "price": 1000,
             "Brand": "Toshiba",
             "model year": 2022
            },
            {
                "name": "oven",
                "price": 750,
                "Brand": "Toshiba",
                "model year": 2021
            },
            {
                "name": "microwave",
                "price": 1250,
                "Brand": "Toshiba",
                "model year": 2020
            },
            {
                "name": "tv",
                "price": 5000,
                "Brand": "Toshiba",
                "model year": 2023
            },
            {
                "name": "Electric fan",
                "price": 650,
                "Brand": "Toshiba",
                "model year": 2022
            }

        ]

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=15, pady=15)
        self.searchButton = tk.Button(self.root, text="buy item", font=("Arial", 15))
        self.searchButton.pack(padx=15, pady=15)
        self.button3 = tk.Button(self.root, text="go to the cart", font=("Arial", 15), command=self.go_to_cart)
        self.button3.pack(padx=15, pady=15)
        # self.show_button_sorted_ascendingly = tk.Button(self.root, text="show sorted items", font=("Arial", 15),
        #                                                 command=self.sorted_data(self.HomeAppliances_data))
        # self.show_button_sorted_ascendingly.pack(padx=15, pady=15)

    def HomeAppliances_data_list(self):
         print(self.HomeAppliances_data)
    def go_to_cart(self):
        self.root.destroy()
        cort.Cart()
    # def sorted_data(self, HomeAppliances_data):
    #     if len(HomeAppliances_data) < 2:
    #         return HomeAppliances_data
    #     else:
    #         self.pivot = HomeAppliances_data[0]
    #         self.less = []
    #         self.greater = []
    #         for i in HomeAppliances_data[1:]:
    #             if i["price"] <= self.pivot["price"]:
    #                 self.less.append(i)
    #             else:
    #                 self.greater.append(i)
    #
    #     return self.sorted_data(self.less) + [self.pivot] + self.sorted_data(self.greater)


class Electronics:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Electronics")
        self.root.geometry("500x500")
        self.root.title("Electronics")
        self.show_button = tk.Button(self.root, text="show items", font=("Arial", 15),
                                     command=self.Electronics_data_list)
        self.show_button.pack(padx=15, pady=15)
        self.Electronics_data = [
            {
                "name": "computers",
                "price": 900,
                "Brand": "Toshiba",
                "model year": 2022
            },
            {
                "name": "iron",
                "price": 250,
                "Brand": "Toshiba",
                "model year": 2022
            },
            {
                "name": "drill",
                "price": 300,
                "Brand": "Toshiba",
                "model year": 2019
            },
            {
                "name": "USB drive",
                "price": 150,
                "Brand": "Toshiba",
                "model year": 2023
            },
            {
                "name": "projector",
                "price": 550,
                "Brand": "Toshiba",
                "model ": 2021
            }
        ]
        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=15, pady=15)
        self.searchButton = tk.Button(self.root, text="buy item", font=("Arial", 15))
        self.searchButton.pack(padx=15, pady=15)
        self.button3 = tk.Button(self.root, text="go to the cart", font=("Arial", 15), command=self.go_to_cart)
        self.button3.pack(padx=15, pady=15)
        # self.show_button_sorted_ascendingly = tk.Button(self.root, text="show sorted items", font=("Arial", 15),
        #                                                 command=self.sorted_data(self.Electronics_data))
        #self.show_button_sorted_ascendingly.pack(padx=15, pady=15)

    def Electronics_data_list(self):
            print(self.HomeAppliances_data)

    def go_to_cart(self):
            self.root.destroy()
            cort.Cart()
class Fashion:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fashion")
        self.root.geometry("500x500")
        self.root.title("Fashion")
        self.show_button = tk.Button(self.root, text="show items", font=("Arial", 15),
                                     command=self.Fashion_data_list)
        self.show_button.pack(padx=15, pady=15)
        self.Fashion_data = [
            {
                "name": "dress",
                "price": 1000,
                "Brand": "Zara",
                "model year": 2022
            },
            {
                "name": "skrit",
                "price": 250,
                "Brand": "Fendi",
                "model year": 2021
            },
            {
                "name": "pants",
                "price": 450,
                "Brand": "Lacoste",
                "model year": 2019
            },
            {
                "name": "bags",
                "price": 150,
                "Brand": "Gucci",
                "model year": 2023
            },
            {
                "name": "shirt",
                "price": 690,
                "Brand": "Lacoste",
                "model ": 2021
            }
        ]
        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=15, pady=15)
        self.searchButton = tk.Button(self.root, text="buy item", font=("Arial", 15))
        self.searchButton.pack(padx=15, pady=15)
        self.button3 = tk.Button(self.root, text="go to the cart", font=("Arial", 15), command=self.go_to_cart)
        self.button3.pack(padx=15, pady=15)
        # self.show_button_sorted_ascendingly = tk.Button(self.root, text="show sorted items", font=("Arial", 15),
        #                                                 command=self.sorted_data(self.Fashion_data))
        # self.show_button_sorted_ascendingly.pack(padx=15, pady=15)

    def Fashion_data_list(self):
        print(self.HomeAppliances_data)

    def go_to_cart(self):
        self.root.destroy()
        cort.Cart()
class Books:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Books")
class Sports:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sport")
