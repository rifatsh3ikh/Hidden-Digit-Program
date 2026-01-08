import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.iconbitmap("logo.ico") 
app.title("Hidden Digit Finder")
app.geometry("400x500")

secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        user_guess = int(entry.get())
        attempts += 1
        
        if user_guess < secret_number:
            result_label.configure(text="Too Low! Try higher 📈")
        elif user_guess > secret_number:
            result_label.configure(text="Too High! Try lower 📉")
        else:
            result_label.configure(text=f"CORRECT! 🎉\nAttempts: {attempts}", text_color="#2ecc71")
            entry.configure(state="disabled")
    except ValueError:
        result_label.configure(text="Enter a number (1-100)!")

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.configure(text="New Game Started!", text_color="white")
    entry.configure(state="normal")
    entry.delete(0, 'end')

# UI
title = ctk.CTkLabel(app, text="Guess The Number", font=("Roboto", 28, "bold"))
title.pack(pady=30)

instruction = ctk.CTkLabel(app, text="I'm thinking of a number between 1 and 100", font=("Arial", 14))
instruction.pack(pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Enter your guess...", width=200, height=45, font=("Arial", 18))
entry.pack(pady=20)

submit_button = ctk.CTkButton(app, text="GUESS", command=check_guess, fg_color="#1f8d49", hover_color="#14375e")
submit_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 18, "bold"))
result_label.pack(pady=20)

reset_button = ctk.CTkButton(app, text="Restart Game", command=reset_game, fg_color="transparent", border_width=2)
reset_button.pack(pady=20)

app.mainloop()