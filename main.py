import tkinter as tk
from tkinter import ttk
import admin
import json
from tkinter import messagebox


def save():
    global data
    file = open("p3.json", "w")
    json.dump(data, file, indent=2)
    file.close()


def loadData():
    try:
        global data
        file = open("p3.json")
        data = json.load(file)
        file.close()
    # to force to create file
    except FileNotFoundError:
        save()


data = []
loadData()


class project_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("team #2 online shopping project")
        self.label = tk.Label(text="LOGIN PAGE", font=("comic"))
        self.label.pack(pady=50)
        self.label_email = tk.Label(text="Email")
        global data
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
            for usr in data:
                if (usr["Email"] == self.email.get() and usr["Password"] == self.password.get()):
                    self.root.destroy()
                    homepage(usr)
                    return
            messagebox.showerror("Error", "email or password may be wrong")

    def register(self):
        self.root.destroy()
        new_account()


class homepage:
    def __init__(self, user):
        self.root = tk.Tk()
        self.root.title("Home Page")
        self.root.geometry("500x500")
        self.usr = user

        self.name = self.usr["Username"]
        self.label = tk.Label(self.root, text=f"welcome, {self.name} choose from categories", font=("Arial", 15))
        self.label.pack(padx=30, pady=35)
        self.options = ["Home appliances", "Electronics", "Fashion", "Books", "Sports"]
        self.selected_option = tk.StringVar()
        self.dropDown = ttk.Combobox(self.root, textvariable=self.selected_option, values=self.options)
        self.dropDown.pack(padx=15, pady=15)
        self.button = tk.Button(self.root, text="ok", font=("Arial", 15), command=self.selected)
        self.button.pack(padx=15, pady=15)
        self.button2 = tk.Button(self.root, text="go back", font=("Arial", 15), command=self.goBack)
        self.button2.place(x=0, y=0)
        self.button3 = tk.Button(self.root, text="show your cart", font=("Arial", 15), command=self.go_to_cart)
        self.button3.pack(padx=15, pady=15)
        self.root.mainloop()

    def selected(self):
        if self.dropDown.get() == "Home appliances":
            self.root.destroy()
            HomeAppliances(self.usr)
            return
        elif self.dropDown.get() == "Electronics":
            self.root.destroy()
            Electronics(self.usr)
            return
        elif self.dropDown.get() == "Fashion":
            self.root.destroy()
            Fashion(self.usr)
            return
        elif self.dropDown.get() == "Books":
            self.root.destroy()
            Books(self.usr)
            return
        elif self.dropDown.get() == "Sports":
            self.root.destroy()
            Sports(self.usr)
            return

    def goBack(self):
        self.root.destroy()
        project_GUI()
        return

    def go_to_cart(self):
        self.root.destroy()
        Cart(self.usr)


class new_account:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x700")
        self.root.title("Team #2 Online Shopping Project")

        # Variables to store user input
        self.username_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.mail_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.governorate_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.national_id_var = tk.StringVar()

        # Create a centered frame to hold the form elements
        self.center_frame = tk.Frame(self.root)
        self.center_frame.pack(expand=True, pady=20)

        # Create labels and entry fields
        self.label_username = tk.Label(self.center_frame, text="Username:")
        self.label_phone = tk.Label(self.center_frame, text="Phone Number:")
        self.label_mail = tk.Label(self.center_frame, text="Email:")
        self.label_gender = tk.Label(self.center_frame, text="Gender:")
        self.label_governorate = tk.Label(self.center_frame, text="Governorate:")
        self.label_password = tk.Label(self.center_frame, text="Password:")
        self.label_age = tk.Label(self.center_frame, text="Age:")
        self.label_national_id = tk.Label(self.center_frame, text="National ID:")

        self.entry_username = tk.Entry(self.center_frame, textvariable=self.username_var)
        self.entry_phone = tk.Entry(self.center_frame, textvariable=self.phone_var)
        self.entry_mail = tk.Entry(self.center_frame, textvariable=self.mail_var)
        self.entry_governorate = tk.Entry(self.center_frame, textvariable=self.governorate_var)
        self.entry_password = tk.Entry(self.center_frame, show="*", textvariable=self.password_var)  # Password field
        self.entry_age = tk.Entry(self.center_frame, textvariable=self.age_var)
        self.entry_national_id = tk.Entry(self.center_frame, textvariable=self.national_id_var)

        # Create radio buttons for gender
        self.radio_male = tk.Radiobutton(self.center_frame, text="Male", variable=self.gender_var, value="Male")
        self.radio_female = tk.Radiobutton(self.center_frame, text="Female", variable=self.gender_var, value="Female")

        # Create a submit button
        self.submit_button = tk.Button(self.center_frame, text="Submit", command=self.register)

        # Layout using pack
        self.label_username.pack(fill='both', padx=10, pady=5)
        self.entry_username.pack(fill='both', padx=10, pady=5)
        self.label_phone.pack(fill='both', padx=10, pady=5)
        self.entry_phone.pack(fill='both', padx=10, pady=5)
        self.label_mail.pack(fill='both', padx=10, pady=5)
        self.entry_mail.pack(fill='both', padx=10, pady=5)
        self.label_gender.pack(fill='both', padx=10, pady=5)
        self.radio_male.pack(fill='both', padx=10, pady=5)
        self.radio_female.pack(fill='both', padx=10, pady=5)
        self.label_governorate.pack(fill='both', padx=10, pady=5)
        self.entry_governorate.pack(fill='both', padx=10, pady=5)
        self.label_password.pack(fill='both', padx=10, pady=5)
        self.entry_password.pack(fill='both', padx=10, pady=5)
        self.label_age.pack(fill='both', padx=10, pady=5)
        self.entry_age.pack(fill='both', padx=10, pady=5)
        self.label_national_id.pack(fill='both', padx=10, pady=5)
        self.entry_national_id.pack(fill='both', padx=10, pady=5)

        self.submit_button.pack(fill='both', padx=10, pady=10)

        self.root.mainloop()

    def register(self):
        username = self.username_var.get()
        phone = self.phone_var.get()
        mail = self.mail_var.get()
        gender = self.gender_var.get()
        governorate = self.governorate_var.get()
        password = self.password_var.get()
        age = self.age_var.get()
        national_id = self.national_id_var.get()

        # Check for missing data
        if not username or not phone or not mail or not gender or not governorate or not password or not age or not national_id:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # Check if age and national ID are integers
        try:
            age = int(age)
            national_id = int(national_id)
            phone = int(phone)
        except ValueError:
            messagebox.showerror("Error", "Age ,phone,and National ID must be integers.")
            return

        # check if user have an acount using the national_id
        if any(usr["National ID"] == national_id for usr in data):
            messagebox.showerror("Error", "this user have already an account")
            return
        else:
            user_data = {
                "Username": username,
                "Phone Number": phone,
                "Email": mail,
                "Gender": gender,
                "Governorate": governorate,
                "Password": password,
                "Age": age,
                "National ID": national_id,
                "cart": []
            }
            data.append(user_data)
            save()
            messagebox.showinfo("Success", "Registration successful!")
            self.root.destroy()
            homepage(user_data)


class HomeAppliances:
    def __init__(self, user):

        self.usr = user

        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("HomeAppliances")
        self.show_button = tk.Button(self.root, text="show items", font=("Arial", 15),
                                     command=self.HomeAppliances_data_list)
        self.show_button.pack(padx=15, pady=15)
        self.cat_data = [
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
        self.label_search = tk.Label(self.root, font=("Arial", 30), text="search for your item")
        self.label_search.pack(padx=15, pady=15)
        self.word = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.word)
        self.entry.pack(padx=5, pady=5)
        # self.string_word = str(self.word)
        # print(self.string_word)
        self.searchButton = tk.Button(self.root, text="search item", font=("Arial", 15), command=self.printed)
        self.searchButton.pack(padx=15, pady=15)
        self.button3 = tk.Button(self.root, text="go to the cart", font=("Arial", 15), command=self.go_to_cart)
        self.button3.pack(padx=15, pady=15)
        self.show_button_sorted_ascendingly = tk.Button(self.root, text="show sorted items", font=("Arial", 15),
                                                        command=self.sorted_data_printed)
        self.show_button_sorted_ascendingly.pack(padx=15, pady=15)
        self.show_button_sorted_dscendingly = tk.Button(self.root, text="show sorted items dscendingly",
                                                        font=("Arial", 15),
                                                        command=self.reverse_sorted_printed)
        self.show_button_sorted_ascendingly.pack(padx=15, pady=15)
        self.button4 = tk.Button(self.root, text="add to cart", font=("Arial", 15), command=self.add_to_cart)
        self.button4.pack(padx=15, pady=15)

    def HomeAppliances_data_list(self):
        print(self.cat_data)

    def go_to_cart(self):
        self.root.destroy()
        Cart(self.usr)

    def add_to_cart(self):
        global data
        item = self.binarysearch(self.sorted_items(self.cat_data), target=self.word.get(), start=0,
                                 end=len(self.cat_data))
        if (item != -1):
            self.usr["cart"].append(item)
            save()
            messagebox.showinfo("Success", "added to cart successfully")
        else:
            messagebox.showinfo("Eroor", "item not found")

    # search(self.binarysearch(self.HomeAppliances_data, self.entry))
    def sorted_data(self, sortList):
        if len(sortList) < 2:
            return sortList
        else:
            pivot = sortList[0]
            less = []
            greater = []
            for i in sortList[1:]:
                if i["price"] <= pivot["price"]:
                    less.append(i)
                else:
                    greater.append(i)
            return self.sorted_data(less) + [pivot] + self.sorted_data(greater)

    def sorted_data_printed(self):
        print(self.sorted_data(self.cat_data))
        return

    def sorted_items(self, List):
        if len(List) < 2:
            return List
        else:
            pivot = List[0]
            less = []
            greater = []
            for i in List[1:]:
                if i["name"] <= pivot["name"]:
                    less.append(i)
                else:
                    greater.append(i)
            return self.sorted_items(less) + [pivot] + self.sorted_items(greater)

    def binarysearch(self, lis, target, start, end):
        if start <= end:
            mid = (start + end) // 2
            if lis[mid]["name"] == target:
                return lis[mid]
            elif lis[mid]["name"] < target:
                return self.binarysearch(lis, target, mid + 1, end)
            elif lis[mid]["name"] > target:
                return self.binarysearch(lis, target, start, mid - 1)
        return -1

    def printed(self):
        print(self.binarysearch(self.sorted_items(self.cat_data), target=self.word.get(), start=0,
                                end=len(self.cat_data)))

    def reverse_sorted(self, List):
        if len(List) < 2:
            return List
        else:
            pivot = List[0]
            less = []
            greater = []
            for i in List[1:]:
                if i["price"] <= pivot["price"]:
                    less.append(i)
                else:
                    greater.append(i)
            return self.reverse_sorted(greater) + [pivot] + self.reverse_sorted(less)

    def reverse_sorted_printed(self):
        print(self.reverse_sorted(self.cat_data))


class Electronics(HomeAppliances):
    def __init__(self, usr):
        super().__init__(usr)
        self.cat_data = [
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


class Fashion(HomeAppliances):
    def __init__(self, usr):
        super().__init__(usr)

        self.cat_data = [
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


class Books(HomeAppliances):
    def __init__(self, usr):
        super().__init__(usr)
        self.cat_data = [{
            "name": "harry poter",
            "price": 30,
            "Brand": "j.k.rolling",
            "model ": 'novel'
        }]


class Sports:
    def __init__(self, usr):
        super().__init__(usr)
        self.cat_data = [{
            "name": "football",
            "price": 60,
            "Brand": "nike",
            "model ": '2023'
        }]


class Cart:
    def __init__(self, usr):
        self.root = tk.Tk()
        self.root.title("Shopping Cart")
        self.root.geometry("500x500")

        global data

        self.usr = usr

        # Create a "Back" button in the top-left corner
        self.back_button = tk.Button(self.root, text="Back", command=self.back_function)
        self.back_button.pack(side=tk.TOP, padx=10, pady=10)  # Position the "Back" button at the top

        # Create a "Delete" button
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_item)
        self.delete_button.pack(side=tk.BOTTOM)  # Position the "Delete" button to the left

        # Create a "Sum" button beside the "Delete" button
        self.sum_button = tk.Button(self.root, text="Sum", command=self.sum_function)
        self.sum_button.pack(side=tk.BOTTOM)  # Position the "Sum" button to the left of the "Delete" button

        # Create a Listbox widget
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        # Create a Scrollbar widget
        self.scrollbar = tk.Scrollbar(self.listbox)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Listbox and Scrollbar to work together
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Create a label to display the selected item's name and price
        self.selected_label = tk.Label(self.root, text="")
        self.selected_label.pack()

        # List of items
        self.items = self.usr["cart"]

        # Populate the Listbox with items (name and price)
        for item in self.items:
            self.listbox.insert(tk.END, f"{item['name']} (${item['price']})")

        self.root.mainloop()

    def delete_item(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No item selected. Please select an item to delete.")
        else:
            item_index = selected_index[0]  # Get the index of the selected item
            self.listbox.delete(item_index)  # Remove the item from the Listbox
            del self.items[item_index]  # Remove the item from the list
            save()

    def sum_function(self):
        # Display a placeholder message box for the "Sum" button
        sum = 0
        for item in self.items:
            sum += item["price"]
        fees = self.transportation_fees()
        messagebox.showinfo("Sum", "the sum is {} \n transport fees is {} \n total is {}".format(sum, fees, sum + fees))

    def back_function(self):
        self.root.destroy()
        homepage(self.usr)

    def transportation_fees(self):
        if self.usr["Governorate"] == "Cairo":
            return 0
        elif (self.usr["Governorate"] == "Alexandria"):
            return 30
        else:
            return 100



project_GUI()