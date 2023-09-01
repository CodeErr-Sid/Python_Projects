from quiz_brain import QuizBrain
from data import question_data

logo='''
________        .__                   ________                       
\_____  \  __ __|__|_______________  /  _____/_____    _____   ____  
 /  / \  \|  |  \  \___   /\___   / /   \  ___\__  \  /     \_/ __ \ 
/   \_/.  \  |  /  |/    /  /    /  \    \_\  \/ __ \|  Y Y  \  ___/ 
\_____\ \_/____/|__/_____ \/_____ \  \______  (____  /__|_|  /\___  >
       \__>              \/      \/         \/     \/      \/     \/
'''
print(logo)

class Question:

  def __init__(self, q_text, q_answer):
    self.text = q_text
    self.answer = q_answer


question_bank = []

for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
 quiz.next_question()