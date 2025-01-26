import tkinter as tk

# Create the application window
app = tk.Tk()
app.title("Register Page")
app.geometry("400x400")

# Username label and entry field
username_label = tk.Label(app, text="User Name")
username_label.pack(pady=5)  # Add padding for better spacing
uname = tk.Entry(app)
uname.pack(pady=5)

# Password label and entry field
password_label = tk.Label(app, text="Password")
password_label.pack(pady=5)
upassword = tk.Entry(app, show="*")  # Mask password input by default
upassword.pack(pady=5)

# Function to toggle password visibility
def toggle_password():
    if upassword.cget("show") == "*":  # If password is hidden
        upassword.config(show="")  # Show password
        toggle_btn.config(text="Hide")  # Update button text
    else:
        upassword.config(show="*")  # Hide password
        toggle_btn.config(text="Show")  # Update button text

# Eye button to toggle password visibility
toggle_btn = tk.Button(app, text="Show", command=toggle_password)
toggle_btn.pack(pady=5)

# Function to save username and password to auth.txt
def save():
    unamesave = uname.get().strip()  # Strip whitespace for clean input
    passwordsave = upassword.get().strip()
    
    if unamesave and passwordsave:  # Ensure fields are not empty
        try:
            with open("auth.txt", "a") as handle:  # Open file in append mode
                handle.write(f"username: {unamesave}, password: {passwordsave}\n")
            status_label.config(text="Registered successfully!", fg="green")
            uname.delete(0, tk.END)  # Clear the username field
            upassword.delete(0, tk.END)  # Clear the password field
        except Exception as e:
            status_label.config(text=f"Error: {e}", fg="red")
    else:
        status_label.config(text="Please fill in all fields.", fg="red")

# Register button
register_button = tk.Button(app, text="Register", command=save)
register_button.pack(pady=10)

# Status label to display messages
status_label = tk.Label(app, text="", fg="red")
status_label.pack(pady=5)

# Run the application
app.mainloop()


