import random
game=["rock","paper","scissors"]
user=(input("Enter your choice(rock,paper,scissors): "))
comp=random.choice(game)
print("Computer chose %s,"%comp)
if comp=="rock":
    if user=="rock":
        print("It's a draw.")
    elif user=="scissors":
        print("You lose!")
    elif user=="paper":
        print("You win!")
elif comp=="scissors":
    if user=="rock":
        print("You win!")
    elif user=="scissors":
        print("It's a draw.")
    elif user=="paper":
        print("You lose!")
elif comp=="paper":
    if user=="rock":
        print("You lose!")
    elif user=="scissors":
        print("You win!")
    elif user=="paper":
        print("It's a draw.")