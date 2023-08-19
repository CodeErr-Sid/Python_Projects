import random

# Ascii charaters 
greeting='''┏┓┏┓┏┓━━━━┏┓━━━━━━━━━━━━━━━━━━━━━┏━━━━┓━━━━━━━━┏━━━━┓┏┓━━━━━━━━━━┏━━━┓━━━━━━━━━━━━━━━━━┏┓
┃┃┃┃┃┃━━━━┃┃━━━━━━━━━━━━━━━━━━━━━┃┏┓┏┓┃━━━━━━━━┃┏┓┏┓┃┃┃━━━━━━━━━━┃┏━┓┃━━━━━━━━━━━━━━━━━┃┃
┃┃┃┃┃┃┏━━┓┃┃━┏━━┓┏━━┓┏┓┏┓┏━━┓━━━━┗┛┃┃┗┛┏━━┓━━━━┗┛┃┃┗┛┃┗━┓┏━━┓━━━━┃┃━┗┛┏━━┓━┏┓┏┓┏━━┓━━━━┃┃
┃┗┛┗┛┃┃┏┓┃┃┃━┃┏━┛┃┏┓┃┃┗┛┃┃┏┓┃━━━━━━┃┃━━┃┏┓┃━━━━━━┃┃━━┃┏┓┃┃┏┓┃━━━━┃┃┏━┓┗━┓┃━┃┗┛┃┃┏┓┃━━━━┗┛
┗┓┏┓┏┛┃┃━┫┃┗┓┃┗━┓┃┗┛┃┃┃┃┃┃┃━┫━━━━━┏┛┗┓━┃┗┛┃━━━━━┏┛┗┓━┃┃┃┃┃┃━┫━━━━┃┗┻━┃┃┗┛┗┓┃┃┃┃┃┃━┫━━━━┏┓
━┗┛┗┛━┗━━┛┗━┛┗━━┛┗━━┛┗┻┻┛┗━━┛━━━━━┗━━┛━┗━━┛━━━━━┗━━┛━┗┛┗┛┗━━┛━━━━┗━━━┛┗━━━┛┗┻┻┛┗━━┛━━━━┗┛
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

'''
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

trophy='''           _____________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""
'''
my_list=[rock,paper,scissors]
# 0 - rock
# 1 - paper
# 2 - scissors

print(f"{greeting}")
print("choices :\n"+">> 0 for Rock.\n"+">> 1 for Paper.\n"+">> 2 for Scisscors.\n")
print("----------------------------------------------------------------------------------")
user_choice=int(input("Enter your choice, To start the game : "))
print("----------------------------------------------------------------------------------")
comp_choice=random.randint(0,2)
# user choice
if user_choice== 0 or user_choice==1 or user_choice==2:
  print(f"\nYour Choice is: \n{my_list[user_choice]}")
  if comp_choice== 0 or comp_choice==1 or comp_choice==2:
   print(f"\nComputers Choice is: \n{my_list[comp_choice]}")
  else:
   print("")
else:
  print("\noops!, It seems like you have entered an invalid choice. ")

print("----------------------------------------------------------------------------------")

#computer choice

# if comp_choice=random.randint(0,2):

# print(f"\nComputers Choice is: \n{my_list[comp_choice]}")
# print("----------------------------------------------------------------------------------")

#logic of the game

if user_choice==comp_choice:
  print("\nGAME DRAW 🙂!")
elif user_choice==0 and comp_choice==1:
  print("\nYOU LOSE 😞")
elif user_choice==0 and comp_choice==2:
  print(f"\nYOU WIN 😃 !\n {trophy}")
elif user_choice==1 and comp_choice==0:
  print(f"\nYOU WIN 😃 !\n {trophy}")
elif user_choice==1 and comp_choice==2:
  print("\nYOU LOSE 😞")
elif user_choice==2 and comp_choice==0:
  print("\nYOU LOSE 😞")
elif user_choice==2 and comp_choice==1:
  print(f"\nYOU WIN 😃 !\n {trophy}")
else:
  print("")

print("----------------------------------------------------------------------------------")

