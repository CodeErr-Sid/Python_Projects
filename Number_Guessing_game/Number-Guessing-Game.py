import random

logo='''

  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               

'''

EASY_LEVEL = 10
HARD_LEVEL = 5



def check_answer(user_guess, answer, turns):
  if user_guess > answer:
    print("Too High !")
    return turns-1
  elif user_guess < answer:
    print("Too Low !")
    return turns-1
  else:
    print(f"You Got It !, The Answer is {answer}.")
    

def set_difficulty():
  level = input("Choose a difficulty, Type 'easy' or hard': ").lower()
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL



def play():
  print(logo)
  print("\nWelcome to The Number Guessing Game !.\n")
  print("I'm Guessing a Number Between 1 and 100.\n")
  turns = set_difficulty()
  print(f"\nYou Have {turns} attempts left.")
  
  answer = random.randint(1,100)
  
  user_guess = 0
  while user_guess != answer:
    
    user_guess =int(input("\nEnter Your Guess: "))
    turns = check_answer(user_guess, answer, turns)
    print(f"\nYou Have {turns} attempts left.")

play()