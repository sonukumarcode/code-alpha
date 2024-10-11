import random
import hangmanstage
# create a list of words
words=["apple","potato","good","lion"]



hint=["fruit","vegetable","compliment","animal"]
life=6
chose_word=random.choice(words)
hint_index=words.index(chose_word)
print(f"it's like a {hint[hint_index]}")


# create a empty list
display=[]
for i in range(len(chose_word)):
    display += "-"
print(display)
# user input
game_over=False
while not game_over:
    guess_letter=input("guess a latter in this columns: ")
    for position in range(len(chose_word)):
        letter=chose_word[position]
        if letter==guess_letter:
            display[position]=guess_letter
    print(display)

    if guess_letter not in chose_word:
        life-= 1
        print(hangmanstage.stage[life])
        if life == 0:
            game_over=True
            print("you lose this match")
            print("better luck next time")
            

    if '-' not in display:
        game_over=True
        print("you won this match")
    
   
               
          