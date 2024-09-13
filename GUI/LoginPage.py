import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image, ImageTk
from Auth.Users import NormalUser

class loginPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login Page")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        # Load and display the image
        self.image = Image.open("logo.png")
        self.image = self.image.resize((150, 150))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.root, image=self.photo, bg="#f0f0f0")
        self.image_label.pack(pady=20)

        self.title_label = tk.Label(self.root, text="Welcome to the Login Page", font=("Arial", 20), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        tk.Label(self.root, text="Email:", bg="#f0f0f0", font=("Arial", 16)).pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=10, padx=20)

        tk.Label(self.root, text="Password:", bg="#f0f0f0", font=("Arial", 16)).pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=10, padx=20)

        self.loginButton = tk.Button(self.root, text="Login", command=self.goToHomePage, bg="#4caf50", fg="white", width=20)
        self.loginButton.pack(pady=20)

        self.root.mainloop()

    def goToHomePage(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            messagebox.showwarning("Input Error", "Please fill in both fields")
            return

        # Check for admin credentials (hard-coded for this example)
        if username == "admin@example.com" and password == "admin123":
            self.admin_login()
            return

        try:
            with open("db.json", "r") as file:
                data = json.load(file)
                users = data.get("users", [])
        except FileNotFoundError:
            messagebox.showerror("Error", "Database not found!")
            return

        user_found = False
        for user_data in users:
            if user_data["email"] == username and user_data["password"] == password:
                logged_in_user = NormalUser(
                    username=user_data["email"],
                    password=user_data["password"],
                    name=user_data["name"],
                    phone_number=user_data["phone_number"],
                    email=user_data["email"],
                    gender=user_data["gender"],
                    governorate=user_data["governorate"],
                    age=user_data["age"],
                    national_id=user_data["national_id"]
                )
                user_found = True
                break

        if user_found:
            messagebox.showinfo("Login Success", f"Welcome, {logged_in_user.get_name()}!")
            self.root.destroy()
            #to the user's home page
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def admin_login(self):
        messagebox.showinfo("Admin Login", "Welcome, Admin!")
        self.root.destroy()
        #  to the admin dashboard

loginPage()
