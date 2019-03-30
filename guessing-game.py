def main():
    animal = "snake"
    while True:
        print("This program is thinking of an animal...")
        answer = input("Can you guess what it is?: ").lower()
        if answer == animal:
            print("Congratulations! You guessed correctly!")
            nextAnswer = question()
            break
        elif answer[0] == "q":
            break
        else:
            print("Your guess was incorrect, try again!")

def question():
    while True:
        nextAnswer = input("Do you like snakes? (y or n): ").lower()
        if nextAnswer == "y":
            print("Me too! They certainly are interesting!")
            break
        elif nextAnswer == "n":
            print("Me neither! They're creepy!")
            break
        else:
            print("That's not what I asked...")
    
main()
