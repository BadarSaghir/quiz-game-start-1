import random


class QuizBrain:

    def __init__(self, q_list):
        """
        :type q_list: List[Question...]
        """
        self.question_no = 0
        self.question_list = q_list

    def next_question(self):
        if self.question_no == 0:
            random.shuffle(self.question_list)

        current_question = self.question_list[self.question_no]
        ans = self.question_list[self.question_no]

        user_ans = input(f"Q{self.question_no + 1} {current_question.text} (True/False) : ")

        self.question_no += 1

        if self.question_no == len(self.question_list):
            self.question_no = 0
            random.shuffle(self.question_list)

       # print(user_ans[0].capitalize(), current_question.answer)

        if user_ans[0].capitalize() == current_question.answer[0]:
            print("Correct")
            return True
        else:
            print("False")
            self.question_no = 0
            return False
