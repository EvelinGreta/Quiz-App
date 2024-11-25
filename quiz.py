from tkinter import *
from tkinter import messagebox

questions = (
    "What language does the anime use for the character's names? ",
    "What does Lügner's name mean? ",
    "What is the name of the festival during which the hero's party witnesses the stars in the night sky? ",
    "What is Frieren's favourite spell? ",
    "What spell does Fern ask from Serie after passing the First-Class Mage Exam? ",
    "What does the Lotus Ring represent? ",
    "What flower does Frieren use to decorate Himmel's statue? ",
    "Whom does Frieren defeat in a one-on-one battle in the first test of First-Class Mage Exam? ",
    "What does Stark's name mean? ",
    "What is Frieren's secret weakness? ",
    "What is the first gift Frieren gifts to Fern? "
)

options = (
    ("A. French", "B. German", "C. English"),
    ("A. Cruel", "B. Evil", "C. Liar"),
    ("A. The Festival of Stars", "B. It was not a festival", "C. The Festival of Falling Lights"),
    ("A. A field of flowers", "B. Hiding Mana", "C. A simple cleaning spell"),
    ("A. Sleep spell", "B. Spell to make clothes clean and spotless", "C. Time-Slowing spell"),
    ("A. Eternal Love", "B. Eternal Bliss", "C. Eternal Memory"),
    ("A. Blue moon weed flowers", "B. Moon-drop lavender", "C. Azure flowers"),
    ("A. Wirbel", "B. Übel", "C. Denken"),
    ("A. Strong", "B. Coward", "C. Proud"),
    ("A. Not understanding the emotions of others", "B. Her love towards Fern", "C. Mimics"),
    ("A. A hair ornament", "B. A bracelet", "C. A staff")
)

answers = ("B", "C", "B", "A", "B", "A", "A", "C", "A", "C", "A")

score = 0
question_num = 0


def show_question():
    if question_num < len(questions):
        question_label.config(text=questions[question_num])
        var.set(0)
        for index, option in enumerate(options[question_num]):
            option_buttons[index].config(text=option)
    else:
        score_percentage = int(score / len(questions) *100)
        messagebox.showinfo("Congratulations!", f"Your score is: {score_percentage}%")
        window.quit()


def submit_answer(event=None):
    global question_num, score
    selected_answer = var.get()

    if selected_answer == 0:
        messagebox.showwarning("No selection", "Please select an option!")
        return

    correct_answer = answers[question_num]
    if chr(64 + selected_answer) == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "Correct answer!")
    else:
        messagebox.showinfo("Incorrect", f"Incorrect answer! The correct answer was {correct_answer}.")
    
    question_num += 1
    show_question()

window = Tk()
window.title("Frieren Trivia")
window_width = 900
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coord = (screen_width // 2) - (window_width // 2)
y_coord = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")
Label(window, text="Welcome to Frieren: Beyond Journey's End Trivia", font=("Arial", 12), fg = "navy").pack(pady=5)

question_label = Label(window, text="", font=("Arial", 14))
question_label.pack(pady=20)

var = IntVar()

option_buttons = []
for i in range(3):
    button = Radiobutton(window, text=f"Option {i+1}", variable=var, value=i+1, font=("Arial", 12))
    button.pack(anchor=W)
    option_buttons.append(button)

submit_button = Button(window, text="Submit", font=("Arial", 12), command=submit_answer)
submit_button.pack(pady=10)

window.bind('<Return>', submit_answer)

show_question()
window.mainloop()