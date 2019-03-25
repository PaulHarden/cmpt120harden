def main():
    animal = "snake"
    while True:
        print("This program is thinking of an animal...")
        answer = input("Can you guess what it is?: ")
        if answer == animal:
            break
        else:
            print("Your guess was incorrect, try again!")

    print("Congratulations! You guessed correctly!")
        
main()
