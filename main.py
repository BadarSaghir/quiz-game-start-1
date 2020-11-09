import data
from question_model import Question
from quiz_brain import QuizBrain

questionBank = []
for question in data.question_data:
    new_question = Question(question["text"], question["answer"])
    # print(new_question.text, new_question.answer)
    questionBank.append(new_question)

quiz = QuizBrain(questionBank)

for start in quiz.question_list:
    while quiz.next_question():
        pass
    if input("Wanna play again (y/n):")[0].capitalize() == 'Y':
        pass
    else:
        break
