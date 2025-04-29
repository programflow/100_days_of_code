from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(self.window, width=300, height=250, background="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, text= "Question goes here!", font=("Arial", 20, "italic"))


        check_mark_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=check_mark_image, borderwidth=0, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        x_mark_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=x_mark_image, borderwidth=0, highlightthickness=0)
        self.false_button.grid(row=2, column=1)




        self.window.mainloop()

