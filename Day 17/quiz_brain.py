# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number].text
        current_answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {current_question} (True/False) ")
        self.check_answer(player_answer, current_answer)



    def check_answer(self, answer, user_answer):
        if answer.lower() == user_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was :{user_answer} ")
        print(f'Your score is: {self.score}/{self.question_number}')

    def game_over(self):
        print("You've completed the quiz.")
        print(f"Your final score is: {self.score}/{self.question_number}")