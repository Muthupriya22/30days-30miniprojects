import tkinter as tk
import random


choices = ["Rock", "Paper", "Scissors"]


user_score = 0
comp_score = 0


def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)
    if user_choice == comp_choice:
        result = "It's a Tie! 😐"
        color = "yellow"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win! 🎉"
        color = "green"
        user_score += 1
    else:
        result = "You Lose! 😢"
        color = "red"
        comp_score += 1

    
    user_label.config(text=f"You: {user_choice}")
    comp_label.config(text=f"Computer: {comp_choice}")
    result_label.config(text=result, fg=color)
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")


def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_label.config(text="You: ")
    comp_label.config(text="Computer: ")
    result_label.config(text="", fg="white")
    score_label.config(text="Score - You: 0 | Computer: 0")

root = tk.Tk()
root.title("Rock Paper Scissors Game 🎮")
root.geometry("450x450")
root.config(bg="#222831")  


title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), fg="white", bg="#222831")
title.pack(pady=20)


user_label = tk.Label(root, text="You: ", font=("Arial", 14), fg="#00ADB5", bg="#222831")
user_label.pack()
comp_label = tk.Label(root, text="Computer: ", font=("Arial", 14), fg="#FF5722", bg="#222831")
comp_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="white", bg="#222831")
result_label.pack(pady=10)
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 14), fg="white", bg="#222831")
score_label.pack(pady=5)


button_frame = tk.Frame(root, bg="#222831")
button_frame.pack()

rock_btn = tk.Button(button_frame, text="🪨 Rock", width=10, font=("Arial", 12, "bold"),
                     bg="#393E46", fg="white", command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10, pady=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", width=10, font=("Arial", 12, "bold"),
                      bg="#00ADB5", fg="white", command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10, pady=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=10, font=("Arial", 12, "bold"),
                         bg="#FF5722", fg="white", command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

reset_btn = tk.Button(root, text="🔄 Reset Game", font=("Arial", 12, "bold"),
                      bg="#FFD369", fg="black", command=reset_game)
reset_btn.pack(pady=15)

root.mainloop()
