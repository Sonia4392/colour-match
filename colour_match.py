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
        self.geometry("450x450")

        # -------------------------
        # Instruction
        # -------------------------
        self.instruction = tk.Label(
            self, 
            text="Click the button that matches the color name!", 
            font=("Arial", 14)
        )
        self.instruction.pack(pady=10)

        # -------------------------
        # Difficulty dropdown
        # -------------------------
        self.difficulty_var = tk.StringVar(value="Medium")
        difficulties = ["Easy", "Medium", "Hard"]

        self.difficulty_menu = tk.OptionMenu(
            self, 
            self.difficulty_var, 
            *difficulties, 
            command=lambda _: self.update_buttons()
        )
        self.difficulty_menu.pack(pady=5)

        # -------------------------
        # Target color label
        # -------------------------
        self.target_color = random.choice(list(colors.keys()))
        self.color_label = tk.Label(self, text=self.target_color, font=("Arial", 22, "bold"))
        self.color_label.pack(pady=20)

        # -------------------------
        # Score system
        # -------------------------
        self.score = 0
        self.score_label = tk.Label(self, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack()

        # -------------------------
        # Start / Reset button
        # -------------------------
        self.start_button = tk.Button(
            self, 
            text="Start Game", 
            font=("Arial", 12),
            command=self.start_game
        )
        self.start_button.pack(pady=10)

        # -------------------------
        # Button frame
        # -------------------------
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=20)

        # Load initial buttons
        self.update_buttons()

        # -------------------------
        # Feedback label
        # -------------------------
        self.feedback = tk.Label(self, text="", font=("Arial", 14))
        self.feedback.pack(pady=10)

    # ------------------------------------------------
    # Rebuild buttons based on difficulty
    # ------------------------------------------------
    def update_buttons(self):
        """Rebuild the buttons based on selected difficulty."""

        # Reset score when difficulty changes
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")

        # Clear old buttons
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        difficulty = self.difficulty_var.get()

        # Choose colors based on difficulty
        if difficulty == "Easy":
            selected_colors = list(colors.items())[:2]
        elif difficulty == "Medium":
            selected_colors = list(colors.items())[:4]
        else:  # Hard
            selected_colors = list(colors.items())

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

        self.pick_new_color()

    # ------------------------------------------------
    # Reset game, score, and pick new color
    # ------------------------------------------------
    def start_game(self):
        """Reset the game, score, and choose a new colour."""
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.feedback.config(text="")
        self.pick_new_color()

        # Change button text from 'Start' to 'Reset' 
        self.start_button.config(text="Reset Game")

    # ------------------------------------------------
    # Pick a new valid colour
    # ------------------------------------------------
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

    # ------------------------------------------------
    # Check answer + update score
    # ------------------------------------------------
    def check_answer(self, chosen):
        """Check if the user selected the correct colour."""
        if chosen == self.target_color:
            self.feedback.config(text="✅ Correct!", fg="green")

            # Increase score
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

            # Move to next color
            self.pick_new_color()
        else:
            self.feedback.config(text="❌ Try again!", fg="red")


# ------------------------------------------------
# Run the game
# ------------------------------------------------
if __name__ == "__main__":
    app = ColorGame()
    app.mainloop()
