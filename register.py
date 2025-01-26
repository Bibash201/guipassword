# import tkinter as tk
# import subprocess

# def save():
#     unamesave = uname.get()
#     passwordsave = upassword.get()
    
#     if unamesave and passwordsave:  # Ensure fields are not empty
#         with open("auth.txt", "a") as handle:  # Open file in append mode
#             handle.write(f"username:{unamesave},password:{passwordsave}\n")
#         status_label.config(text="Registered successfully!", fg="green")
#         uname.delete(0, tk.END)  # Clear the username field
#         upassword.delete(0, tk.END)  # Clear the password field
#     else:
#         status_label.config(text="Please fill in all fields.", fg="red")

# def toggle_password():
#     if upassword.cget("show") == "*":
#         upassword.config(show="")
#         toggle_btn.config(text="Hide")
#     else:
#         upassword.config(show="*")
#         toggle_btn.config(text="Show")

# def open_login_gui():
#     subprocess.Popen(["python", "login.py"])  # Open login GUI using subprocess

# # Create registration GUI
# app = tk.Tk()
# app.title("Register Page")
# app.geometry("400x400")

# username_label = tk.Label(app, text="User Name")
# username_label.pack()
# uname = tk.Entry(app)
# uname.pack()

# password_label = tk.Label(app, text="Password")
# password_label.pack()
# upassword = tk.Entry(app, show="*")  # Mask password input
# upassword.pack()

# toggle_btn = tk.Button(app, text="Show", command=toggle_password)
# toggle_btn.pack()

# register_button = tk.Button(app, text="Register", command=save)
# register_button.pack()

# status_label = tk.Label(app, text="")
# status_label.pack()

# login_window_button = tk.Button(app, text="Go to Login", command=open_login_gui)
# login_window_button.pack()

# app.mainloop()

import tkinter as tk
import re
import subprocess  # Import subprocess module to open the login GUI

def validate_password(password):
    # Regular expression for password validation
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(pattern, password):
        return True
    return False

def save():
    unamesave = uname.get()
    passwordsave = upassword.get()
    
    if unamesave and passwordsave:  # Ensure fields are not empty
        if not validate_password(passwordsave):
            status_label.config(text="Password must contain at least 1 capital letter, 1 lowercase letter, 1 number, and 1 symbol.", fg="red")
        else:
            with open("auth.txt", "a") as handle:  # Open file in append mode
                handle.write(f"username:{unamesave},password:{passwordsave}\n")
            status_label.config(text="Registered successfully!", fg="green")
            uname.delete(0, tk.END)  # Clear the username field
            upassword.delete(0, tk.END)  # Clear the password field
    else:
        status_label.config(text="Please fill in all fields.", fg="red")

def clear_status_label(event=None):
    # Clear the status label when the user starts typing
    status_label.config(text="")

def toggle_password():
    if upassword.cget("show") == "*":
        upassword.config(show="")
        toggle_btn.config(text="Hide")
    else:
        upassword.config(show="*")
        toggle_btn.config(text="Show")

def open_login_gui():
    subprocess.Popen(["python", "login.py"])  # Open login GUI using subprocess

# Create registration GUI
app = tk.Tk()
app.title("Register Page")
app.geometry("400x400")

username_label = tk.Label(app, text="User Name")
username_label.pack()
uname = tk.Entry(app)
uname.pack()
uname.bind("<Key>", clear_status_label)  # Bind keypress event to clear status label

password_label = tk.Label(app, text="Password")
password_label.pack()
upassword = tk.Entry(app, show="*")  # Mask password input
upassword.pack()
upassword.bind("<Key>", clear_status_label)  # Bind keypress event to clear status label

# Toggle button to show/hide password
toggle_btn = tk.Button(app, text="Show", command=toggle_password)
toggle_btn.pack()

register_button = tk.Button(app, text="Register", command=save)
register_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()

login_window_button = tk.Button(app, text="Go to Login", command=open_login_gui)
login_window_button.pack()

app.mainloop()
