class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.questions = questions

    def still_has_questions(self):
        return len(self.questions) > self.question_number

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"You current score is: {self.score}/{self.question_number}")
        print("-" * 40)
