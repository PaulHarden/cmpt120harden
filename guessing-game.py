def guessingGame():
    animal = "snake"
    while True:
        answer = input("This program is thinking of an animal... What is it?: ")
        if answer == animal:
            print("Congratulations! You guessed correctly!")
            break
        


        

guessingGame()
