# I acknowledge the use of Microsoft Copilot to assist in creating this code file.
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
        self.geometry("450x350")

        # Instruction
        self.instruction = tk.Label(
            self, 
            text="Click the button that matches the color name!", 
            font=("Arial", 14)
        )
        self.instruction.pack(pady=10)

        # Difficulty dropdown
        self.difficulty_var = tk.StringVar(value="Medium")
        difficulties = ["Easy", "Medium", "Hard"]

        self.difficulty_menu = tk.OptionMenu(
            self, 
            self.difficulty_var, 
            *difficulties, 
            command=lambda _: self.update_buttons()
        )
        self.difficulty_menu.pack(pady=5)

        # Display the target color name
        self.target_color = random.choice(list(colors.keys()))
        self.color_label = tk.Label(self, text=self.target_color, font=("Arial", 22, "bold"))
        self.color_label.pack(pady=20)

        # Button frame
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=20)

        # Load buttons based on difficulty
        self.update_buttons()

        # Feedback message
        self.feedback = tk.Label(self, text="", font=("Arial", 14))
        self.feedback.pack(pady=10)

    def update_buttons(self):
        """Rebuild the buttons based on selected difficulty."""
        # Clear old buttons
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        difficulty = self.difficulty_var.get()

        if difficulty == "Easy":
            selected_colors = list(colors.items())[:2]       # 2 colors
        elif difficulty == "Medium":
            selected_colors = list(colors.items())[:4]       # 4 colors
        else:
            selected_colors = list(colors.items())           # all colors

        # Create new buttons
        for name, hexcode in selected_colors:
            btn = tk.Button(
                self.button_frame, 
                text=name, 
                bg=hexcode, 
                width=10,
                command=lambda n=name: self.check_answer(n)
            )
            btn.pack(side="left", padx=5)

        # Pick a valid color based on difficulty
        self.pick_new_color()

    def pick_new_color(self):
        """Select a new random color depending on difficulty."""
        difficulty = self.difficulty_var.get()

        if difficulty == "Easy":
            available = list(colors.keys())[:2]
        elif difficulty == "Medium":
            available = list(colors.keys())[:4]
        else:
            available = list(colors.keys())

        self.target_color = random.choice(available)
        self.color_label.config(text=self.target_color)

    def check_answer(self, chosen):
        """Check if the user clicked the correct color."""
        if chosen == self.target_color:
            self.feedback.config(text="✅ Correct!", fg="green")
            self.pick_new_color()
        else:
            self.feedback.config(text="❌ Try again!", fg="red")


# Run the game
if __name__ == "__main__":
    app = ColorGame()
    app.mainloop()
