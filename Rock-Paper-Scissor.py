import random

rock = '''
      ___
---'   __\__
      (_)___)
      (_)___)
      (_)__)
---.__(_)_)
'''

paper = '''
    _______
---'   __(_)____
          ____(_)
          _____(_)
         _____(_)
---.________(_)
'''

scissors = '''
    _______
---'  ___(_)____
          ____(_)
       ________(_)
      (____)
---.__(___)
'''

#Write your code below this line 👇
lose = False
while lose == False:

    games_images = [rock, paper, scissors]

    user_choice= int(input("What do you choose?\nType 0 for Rock\nType 1 for Paper \nType 2 for Scissors\n"))

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
        print("\n"*5)
    else: 
        print(games_images[user_choice])

        Computer_choice= random.randint(0,2)
        print(games_images[Computer_choice])
        print(f"Computer chose {Computer_choice}")

    
        if user_choice == 0 and Computer_choice == 2:
            lose = True
            print("You win!")
    
        elif Computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif Computer_choice > user_choice:
            print("You lose")
        elif user_choice > Computer_choice:
            print("You win!")
            lose = True
        elif Computer_choice == user_choice:
            print("It's a draw")
        print("\n"*5)
