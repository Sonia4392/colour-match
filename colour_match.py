import tkinter as tk
import random

# Color dictionary: name → hex code
colors = {
    "Red": "red",
    "Blue": "blue",
    "Green": "green",
    "Yellow": "yellow",
    "Purple": "purple",
    "Orange": "orange"
}

class ColorGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Color Match Game")
        self.geometry("400x300")
        
        # Instruction label
        self.instruction = tk.Label(self, text="Click the button that matches the color name!", font=("Arial", 14))
        self.instruction.pack(pady=10)
        
        # Display random color name
        self.target_color = random.choice(list(colors.keys()))
        self.color_label = tk.Label(self, text=self.target_color, font=("Arial", 20, "bold"))
        self.color_label.pack(pady=20)
        
        # Frame for buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=20)
        
        # Create buttons for each color
        for name, hexcode in colors.items():
            btn = tk.Button(self.button_frame, text=name, bg=hexcode, width=10, command=lambda n=name: self.check_answer(n))
            btn.pack(side="left", padx=5)
        
        # Feedback label
        self.feedback = tk.Label(self, text="", font=("Arial", 14))
        self.feedback.pack(pady=10)

    def check_answer(self, chosen):
        if chosen == self.target_color:
            self.feedback.config(text="✅ Correct!", fg="green")
        else:
            self.feedback.config(text="❌ Try again!", fg="red")

# Run the game
if __name__ == "__main__":
    app = ColorGame()
    app.mainloop()
