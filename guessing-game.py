def main():
    animal = "snake"
    while True:
        print("This program is thinking of an animal...")
        answer = input("Can you guess what it is?: ").lower()
        if answer == animal:
            print("Congratulations! You guessed correctly!")
            break
        elif answer == "quit":
            break
        else:
            print("Your guess was incorrect, try again!")
        
main()
