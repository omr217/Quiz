from question_model import Question
from data import question_data

for q_i in question_data:
    questions = Question('self','q_text')
    answers = Question('self','q_answer')

    question_bank = [questions,answers]
    print(question_bank)

