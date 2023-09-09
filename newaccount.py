import tkinter as tk
from tkinter import messagebox
import Homepage
import json
class new_account:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x700")
        self.root.title("Team #2 Online Shopping Project")
        self.data = []
        self.loadData()        

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
        
        #check if user have an acount using the national_id
        if any(usr["National ID"] == national_id for usr in self.data):
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
                "National ID": national_id
            }
            self.data.append(user_data)
            self.save()
            messagebox.showinfo("Success", "Registration successful!")
            self.root.destroy()
            Homepage.homepage(user_data)



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