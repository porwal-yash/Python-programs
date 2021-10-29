import random
Rock =""""
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

number = int(input("enter any number : "))
random.seed(number)

any =random.randint(0,2)

if any ==0:
    print(Rock)
elif any ==1:
    print(Paper)
elif any ==2:
    print(Scissors)

computer = random.randint(0,2)

if computer ==0:
    print(Rock)
elif computer ==1:
    print(Paper)
elif computer ==2:
    print(Scissors)

if any ==0 and computer==2:
    print("You win")
elif any==1 and computer==0:
    print("You win")
elif any==2 and computer==1:
    print("You win")
elif any == computer:
    print("Draw")
else:
    print("You lose")
