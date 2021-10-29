import random

from hangman_words import word_list
from hangman_art import logo
print(logo)
chossen_word = random.choice(word_list)
print(chossen_word)

life =6
end_of_game=False

display =[]

for letter in range(len(chossen_word)):
    display.append("_")
    # print(display)

while not end_of_game:
    guess = input("Enter a guess: ")

    if guess in display:
        print(f"You guess {guess} which is already in the list")

    for position in range(len(chossen_word)):
        letter =chossen_word[position]
        if letter==guess:
            display[position]=letter
    

    if guess not in chossen_word:
        print("You guess it wrong so you lose a life")
        life= life-1
        print(f"Total life remaining {life}")
        if life==0:
            end_of_game=True
            print("You lose")
    if "_"  not in display:
        end_of_game=True
        print("You win")
    
    print(display)
# for letter in chossen_word:
#     if letter==guess:
#         print("Right")
#     else:
#         print("Wrong")
    from hangman_art import stages
    print(stages[life])