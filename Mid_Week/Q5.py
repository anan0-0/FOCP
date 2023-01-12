import random
cards=["8S","6S","TD","KC","TC","AH","3H","AS","JS","5C","2D","4D","AC","TH",
"KH","2S","8C","6H","6C","8D","2C","JH","4H","KD","3S","AD","2H","7D","5D","9D",
"4S","5H","TS","JC","7C","QH","3D","QC","7H","5S","QD","9S","3C","9C","QS","4C","9H","8H","6D","KS","JD","7S"]
play=["North","South","East","West"]
Aos=""
print("Creating pack of cards....")
print("Shuffling and Dealing....")
print("Four Hands....")
for i in play:
    print(f"{i}--> ",end='')
    for j in range(13):
        card=random.choice(cards)
        print(card," ",end='')
        cards.remove(card)
        if(card=="AS"):
            Aos=i
    print("\n")
print("Looking for the Ace of Spades...")
print(f"{Aos} player has it!")



