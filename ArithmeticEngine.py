def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()
        if cmd == "add" or cmd =="mult" or cmd =="sub" or cmd == "div":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if cmd == "add":
                result = num1 + num2
            elif cmd == "sub":
                result = num1 - num2
            elif cmd == "mult":
                result = num1 * num2
            elif cmd == "div":
                result = num1 // num2
            print("The result is " + str(result) + ".\n")
            break
        elif cmd == "quit":
            break
        else:
            print("That is not a valid command...")
    
def main():
    showIntro()
    doLoop()
    showOutro()

main()
