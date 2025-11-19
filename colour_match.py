# I acknowledge the use of Microsoft Copilot to assist in creating this code file.
import tkinter as tk
import random

# ----------------------------------------------------------
# Color dictionary: maps color names to their hex values
# ----------------------------------------------------------
colors = {
    "Red": "red",
    "Blue": "blue",
    "Green": "green",
    "Yellow": "yellow",
    "Purple": "purple",
    "Orange": "orange"
}

class ColorGame(tk.Tk):
    """
    A simple GUI-based colour matching game using Tkinter.
    The player must click the button that matches the colour name.
    Features include difficulty levels, scoring, countdown timer,
    start/reset functionality, and game over state.
    """

    def __init__(self):
        """Initialises the main window, UI layout, and game variables."""
        super().__init__()
        self.title("Color Match Game")
        self.geometry("450x500")

        # -------------------------
        # Instruction label
        # -------------------------
        self.instruction = tk.Label(
            self,
            text="Click the button that matches the color name!",
            font=("Arial", 14)
        )
        self.instruction.pack(pady=10)

        # -------------------------
        # Difficulty dropdown menu
        # -------------------------
        self.difficulty_var = tk.StringVar(value="Medium")
        difficulties = ["Easy", "Medium", "Hard"]

        self.difficulty_menu = tk.OptionMenu(
            self,
            self.difficulty_var,
            *difficulties,
            command=lambda _: self.update_buttons()  # Refresh buttons when difficulty changes
        )
        self.difficulty_menu.pack(pady=5)

        # -------------------------
        # Target colour display
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
        # Countdown timer label
        # -------------------------
        self.time_left = 30  # Timer starts at 30 seconds
        self.timer_label = tk.Label(self, text=f"Time: {self.time_left}", font=("Arial", 14))
        self.timer_label.pack()

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
        # Frame for colour buttons
        # -------------------------
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=20)

        # Create initial set of buttons
        self.update_buttons()

        # -------------------------
        # Feedback label (Correct / Incorrect / Game Over)
        # -------------------------
        self.feedback = tk.Label(self, text="", font=("Arial", 14))
        self.feedback.pack(pady=10)

    # ------------------------------------------------
    # BUILD BUTTONS BASED ON DIFFICULTY
    # ------------------------------------------------
    def update_buttons(self):
        """
        Regenerates the colour buttons depending on the selected difficulty level.
        Also resets the score whenever difficulty changes.
        """
        # Reset score
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")

        # Clear existing buttons
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        difficulty = self.difficulty_var.get()

        # Select subset of colours based on difficulty
        if difficulty == "Easy":
            selected_colors = list(colors.items())[:2]
        elif difficulty == "Medium":
            selected_colors = list(colors.items())[:4]
        else:
            selected_colors = list(colors.items())

        # Create colour buttons dynamically
        for name, hexcode in selected_colors:
            btn = tk.Button(
                self.button_frame,
                text=name,
                bg=hexcode,
                width=10,
                command=lambda n=name: self.check_answer(n)
            )
            btn.pack(side="left", padx=5)

        # Update target colour after buttons change
        self.pick_new_color()

    # ------------------------------------------------
    # START OR RESET THE GAME
    # ------------------------------------------------
    def start_game(self):
        """
        Resets the entire game state:
        - Resets score
        - Reactivates buttons
        - Restarts countdown timer
        - Picks a new colour
        """
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.feedback.config(text="")

        # Re-enable colour buttons in case they were disabled
        for widget in self.button_frame.winfo_children():
            widget.config(state="normal")

        # Reset timer
        self.time_left = 30
        self.timer_label.config(text=f"Time: {self.time_left}")

        # Start countdown timer
        self.run_timer()

        # Change button text after first start
        self.start_button.config(text="Reset Game")

        # Pick a new colour
        self.pick_new_color()

    # ------------------------------------------------
    # COUNTDOWN TIMER
    # ------------------------------------------------
    def run_timer(self):
        """
        Handles the countdown timer using Tkinter's after() method.
        Calls game_over() when timer reaches zero.
        """
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.after(1000, self.run_timer)  # Run again after 1 second
        else:
            self.game_over()

    # ------------------------------------------------
    # GAME OVER STATE
    # ------------------------------------------------
    def game_over(self):
        """
        Triggers when the timer reaches zero.
        Disables all buttons and displays 'Game Over'.
        """
        self.feedback.config(text="⛔ Game Over!", fg="red")

        # Disable all buttons to stop gameplay
        for widget in self.button_frame.winfo_children():
            widget.config(state="disabled")

    # ------------------------------------------------
    # PICK A NEW TARGET COLOUR
    # ------------------------------------------------
    def pick_new_color(self):
        """
        Chooses a random colour name based on the difficulty level
        and updates the display.
        """
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
    # CHECK ANSWER
    # ------------------------------------------------
    def check_answer(self, chosen):
        """
        Checks whether the selected button matches the displayed colour name.
        Updates score and gives feedback.
        """
        if chosen == self.target_color:
            self.feedback.config(text="✅ Correct!", fg="green")

            # Increase score
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

            # Pick next colour
            self.pick_new_color()
        else:
            self.feedback.config(text="❌ Try again!", fg="red")


# ------------------------------------------------
# Run the game
# ------------------------------------------------
if __name__ == "__main__":
    app = ColorGame()
    app.mainloop()
