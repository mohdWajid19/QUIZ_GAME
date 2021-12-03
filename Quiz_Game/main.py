from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from replit import clear
from art import logo

question_bank = []

for questions in question_data:
    question_bank.append(Question(questions['question'],questions['correct_answer']))

#  or do the same using other logic as 
'''
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['question'],question_data[i]['correct_answer']))
'''
clear()
print(logo)
quiz = QuizBrain(question_bank)
while quiz.has_next_question():
    quiz.next_question()

print("You've Successfully Completed The Quiz,")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
