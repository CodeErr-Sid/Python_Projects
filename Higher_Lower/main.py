from art import logo,vs
from game_data import data
import random

#display art


def format_data(account):
  a_name = account["name"]
  a_desc = account["description"]
  a_country = account["country"]
  return f" {a_name}, a {a_desc}, from {a_country}"


def check_answer(guess, follower_a, follower_b):
   if follower_a > follower_b:
     return guess == "a"
   else:
     return guess == "b"

#Generate a random account from the game data
print(logo)
score = 0
game_should_continue = True
acc_b = random.choice(data)

while game_should_continue:
  acc_a = acc_b
  acc_b = random.choice(data)
  while acc_a == acc_b:
    acc_b = random.choice(data)
  
  #Format The account data into printable format
  
  print(f"Compare A: {format_data(acc_a)}")
  print(vs)
  print(f"Against B: {format_data(acc_b)}")
  
  #ask user for a guess
  guess = input("\nWho has more followers? Type 'A' or 'B:': ").lower()
  
  #check if user is correct
  ##Get follower count of each account
  ### use if to check answer
  follower_a = acc_a["follower_count"]
  follower_b = acc_b["follower_count"]
  
  is_correct = check_answer(guess, follower_a, follower_b)

  if is_correct:
    score+=1
    print(f"\nYou're Right! , Current Score: {score} ")
  else:
    game_should_continue = False
    print(f"\nYou're Wrong! , Final Score: {score}")
      