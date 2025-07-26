import tkinter as tk
from tkinter import messagebox
import random

# Hangman ASCII stages for visual feedback
stages = [
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n========="
]

# Word list (you can expand it as needed)
word_list = ["python", "orange", "banana", "mango", "grape", "watermelon", "peach", "dragonfruit"]

# Main Hangman class
class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Hangman Game")
        self.master.configure(bg="#fefbd8")

        self.word = random.choice(word_list).lower()
        self.correct_letters = []
        self.wrong_letters = []
        self.lives = len(stages) - 1

        self.setup_ui()

    def setup_ui(self):
        # Hangman visual
        self.canvas = tk.Label(self.master, text=stages[self.lives], font=("Courier", 16), bg="#fefbd8", fg="#333")
        self.canvas.pack(pady=10)

        # Word placeholder
        self.word_display = tk.Label(self.master, text="_ " * len(self.word), font=("Helvetica", 24), bg="#fefbd8")
        self.word_display.pack(pady=10)

        # Keyboard buttons
        frame = tk.Frame(self.master, bg="#fefbd8")
        frame.pack()

        self.buttons = {}
        for i, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
            btn = tk.Button(frame, text=char.upper(), width=4, font=("Arial", 14), command=lambda c=char: self.guess(c))
            btn.grid(row=i // 9, column=i % 9, padx=3, pady=3)
            self.buttons[char] = btn

        # Reset button
        tk.Button(self.master, text="Restart Game", font=("Arial", 12), command=self.restart_game).pack(pady=10)

    def guess(self, char):
        if char in self.correct_letters or char in self.wrong_letters:
            return

        if char in self.word:
            self.correct_letters.append(char)
        else:
            self.wrong_letters.append(char)
            self.lives -= 1

        self.update_ui()
        self.check_game_over()

    def update_ui(self):
        # Update Hangman art
        self.canvas.config(text=stages[self.lives])

        # Update word display
        display = " ".join([letter if letter in self.correct_letters else "_" for letter in self.word])
        self.word_display.config(text=display)

        # Disable used buttons
        for char in self.correct_letters + self.wrong_letters:
            self.buttons[char].config(state="disabled", disabledforeground="gray")

    def check_game_over(self):
        if self.lives == 0:
            self.reveal_word()
            messagebox.showerror("Game Over", f"You lost! The word was: {self.word.upper()}")
            self.disable_all_buttons()

        elif all([letter in self.correct_letters for letter in self.word]):
            messagebox.showinfo("🎉 You Win!", f"Congratulations! The word was: {self.word.upper()}")
            self.disable_all_buttons()

    def disable_all_buttons(self):
        for btn in self.buttons.values():
            btn.config(state="disabled")

    def reveal_word(self):
        display = " ".join(self.word)
        self.word_display.config(text=display)

    def restart_game(self):
        self.word = random.choice(word_list).lower()
        self.correct_letters.clear()
        self.wrong_letters.clear()
        self.lives = len(stages) - 1

        self.canvas.config(text=stages[self.lives])
        self.word_display.config(text="_ " * len(self.word))

        for btn in self.buttons.values():
            btn.config(state="normal", fg="black")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    HangmanGame(root)
    root.mainloop()
