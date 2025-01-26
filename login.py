import tkinter as tk

def validate_login():
    entered_username = login_uname.get()
    entered_password = login_upassword.get()
    
    if entered_username and entered_password:
        try:
            with open("auth.txt", "r") as handle:
                credentials = handle.readlines()
                for line in credentials:
                    if "username:" in line and "password:" in line:  # Check format
                        stored_username = line.split("username:")[1].split(",")[0].strip()
                        stored_password = line.split("password:")[1].strip()
                        if entered_username == stored_username and entered_password == stored_password:
                            open_welcome_window()
                            return
                login_status_label.config(text="Invalid username or password.", fg="red")
        except FileNotFoundError:
            login_status_label.config(text="auth.txt file not found.", fg="red")
    else:
        login_status_label.config(text="Please fill in all fields.", fg="red")

def clear_status_label(event=None):
    # Clear the status label when the user starts typing
    login_status_label.config(text="")


def open_welcome_window():
    # login_app.destroy()  # Close the login window
    welcome_app = tk.Tk()
    welcome_app.title("Welcome")
    welcome_app.geometry("400x200")
    
    welcome_label = tk.Label(welcome_app, text="Welcome to Site", font=("Arial", 20))
    welcome_label.pack(pady=50)
    
    welcome_app.mainloop()

def toggle_password():
    if login_upassword.cget("show") == "*":
        login_upassword.config(show="")
        toggle_btn.config(text="Hide")
    else:
        login_upassword.config(show="*")
        toggle_btn.config(text="Show")

# Create login GUI
login_app = tk.Tk()
login_app.title("Login Page")
login_app.geometry("400x400")

login_username_label = tk.Label(login_app, text="User Name")
login_username_label.pack()
login_uname = tk.Entry(login_app)
login_uname.pack()
login_uname.bind("<Key>", clear_status_label)  # Bind keypress event to clear status label

login_password_label = tk.Label(login_app, text="Password")
login_password_label.pack()
login_upassword = tk.Entry(login_app, show="*")  # Mask password input
login_upassword.pack()
login_upassword.bind("<Key>", clear_status_label)  # Bind keypress event to clear status label

# Toggle button to show/hide password
toggle_btn = tk.Button(login_app, text="Show", command=toggle_password)
toggle_btn.pack()

login_button = tk.Button(login_app, text="Login", command=validate_login)
login_button.pack()

login_status_label = tk.Label(login_app, text="")
login_status_label.pack()

login_app.mainloop()
