import tkinter as tk
from tkinter import messagebox

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI Application")
        self.root.geometry("400x300")

        # Create and pack widgets
        self.label = tk.Label(root, text="Welcome to Simple GUI!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Click Me!", command=self.button_click)
        self.button.pack(pady=10)

        self.counter = 0
        self.counter_label = tk.Label(root, text="Counter: 0")
        self.counter_label.pack(pady=10)

        self.increment_button = tk.Button(root, text="Increment Counter", command=self.increment_counter)
        self.increment_button.pack(pady=10)

    def button_click(self):
        text = self.entry.get() or "No text entered!"
        messagebox.showinfo("Message", text)

    def increment_counter(self):
        self.counter += 1
        self.counter_label.config(text=f"Counter: {self.counter}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGUI(root)
    root.mainloop() 