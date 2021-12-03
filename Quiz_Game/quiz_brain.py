class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        

    def has_next_question(self):
        return self.question_number < len(self.question_list)


    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Yoo!! You Got it")
        else:
            print("Oops... That's a wrong answer")
        print(f"The Correct Answer is {correct_answer}")
        print(f"Your Current Score Is {self.score}/{self.question_number} \n\n")


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(current_question.answer[0])
        user_answer = input(f"Q.{self.question_number}: {current_question.text}  (T/F) :: ")
        self.check_answer(user_answer,current_question.answer[0])   
    

    




