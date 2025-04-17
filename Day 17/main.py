from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


# Used a lit comprehension to create a list of question object
question_bank =[Question(item["question"],item["correct_answer"]) for item in question_data]

# start a new quizBrain object
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


quiz.game_over()