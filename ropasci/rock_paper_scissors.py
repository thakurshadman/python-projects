import random

rps_dict = {'1': """
Rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
            '2':
            """
Paper!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
            '3': """
Scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
            }
while 1:
    try:
        computer = str(random.randint(1, 3))
        user_input = input("Enter 1 for rock, 2 for paper, or 3 for scissors: ")
        print("User:")
        print(rps_dict[user_input])
        print("Computer:")
        print(rps_dict[computer])

        if(user_input == computer):
            print("DRAW!\n")

        elif(user_input == '1' and computer == '3'):
            print("You Win!\n")
        elif(user_input == '3' and computer == '2'):
            print("You Win!\n")
        elif(user_input == '2' and computer == '1'):
            print("You Win!\n")
        else:
            print("You Lose!\n")

    except:
        print("Error! Invalid Input!\n")

