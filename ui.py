from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain



THEME_COLOR = "#375362"
    

class Quizinterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}",
                                 foreground='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="This is canvas text",
            fill=THEME_COLOR,
            font=("Arial", 22, "italic"))

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()



        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()

            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
        else:
            messagebox.showinfo(title="GAME OVER",
                                message=f"Correct Answer: {self.quiz.score} \n"
                                        f"Total Question: {self.quiz.question_number}")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the question!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")


    # def question_finished(self):
    #     if self.quiz.question_number >= parameters["amount"]:
    #
    #
    #         return True
    #     else:
    #         return False
