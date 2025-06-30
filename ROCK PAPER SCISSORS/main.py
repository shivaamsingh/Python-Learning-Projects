import sys
import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("400x400")

        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["Rock", "Paper", "Scissors"]

        # Create widgets
        self.title_label = tk.Label(self.window, text="Rock Paper Scissors", font=('Arial', 16))
        self.title_label.pack(pady=20)

        # Score display
        self.score_label = tk.Label(self.window,
                                    text=f"Score - You: {self.player_score} Computer: {self.computer_score}",
                                    font=('Arial', 12))
        self.score_label.pack(pady=10)

        # Result display
        self.result_label = tk.Label(self.window, text="Choose your move!", font=('Arial', 12))
        self.result_label.pack(pady=20)

        # Computer's choice display
        self.computer_label = tk.Label(self.window, text="", font=('Arial', 12))
        self.computer_label.pack(pady=10)

        # Buttons frame
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=20)

        # Create choice buttons
        for choice in self.choices:
            button = tk.Button(button_frame, text=choice, width=10,
                               command=lambda c=choice: self.play_round(c))
            button.pack(side=tk.LEFT, padx=5)

        # Reset button
        self.reset_button = tk.Button(self.window, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=20)

    def play_round(self, player_choice):
        computer_choice = random.choice(self.choices)
        self.computer_label.config(text=f"Computer chose: {computer_choice}")

        # Determine winner
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif ((player_choice == "Rock" and computer_choice == "Scissors") or
              (player_choice == "Paper" and computer_choice == "Rock") or
              (player_choice == "Scissors" and computer_choice == "Paper")):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        # Update display
        self.result_label.config(text=f"You chose {player_choice}. {result}")
        self.score_label.config(text=f"Score - You: {self.player_score} Computer: {self.computer_score}")

        # Check for game end
        if self.player_score == 5 or self.computer_score == 5:
            winner = "You win the game!" if self.player_score == 5 else "Computer wins the game!"
            play_again = messagebox.askyesno("Game Over",
                                             f"{winner}\nWould you like to play again?")
            if play_again:
                self.reset_game()
            else:
                self.window.quit()

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.result_label.config(text="Choose your move!")
        self.computer_label.config(text="")
        self.score_label.config(text=f"Score - You: {self.player_score} Computer: {self.computer_score}")

    def run(self):
        self.window.mainloop()


def main():
    game = RockPaperScissors()
    game.run()


if __name__ == "__main__":
    main()