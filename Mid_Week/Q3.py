password="python"
while True:
    pwd=input("Greetings! What is the password? ")
    if pwd==password:
        print("Correct! You may enter.")
        break
    else:
        print("Incorrect! You may try again.")
