import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Hello, welcome to your Python desktop application!")

# Create the main application window
root = tk.Tk()
root.title("Python Desktop App")

# Create a label
label = tk.Label(root, text="Click the button to show a message!")
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Click me!", command=show_message)
button.pack(pady=5)

# Run the application
root.mainloop()
