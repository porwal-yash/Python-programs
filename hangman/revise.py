import random
from hangman_art import logo
print(logo)

from hangman_words import word_list

choosen = random.choice(word_list)
print(choosen)

life =6

display =[]
for i in range(len(choosen)):
    display.append("_")
print(display)

end_of_game = False
while not end_of_game:
    user =input("enter a char: ")

    if user in display:
        print("You already guessed it")

    for position in range(len(choosen)):
        letter =choosen[position]
        if letter==user:
            display[position] = letter
    if user not in choosen:
        life=life-1
        print(f"You guessed it wrong so you lose a life life remaining {life}")
        if life==0:
            end_of_game=True
            print("Because of no life you lose")

    if "_" not in display:
        end_of_game=True
        print("You win")

    print(display)

    from hangman_art import stages
    print(stages[life])