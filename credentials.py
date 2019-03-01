# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Paul Harden
# Created: 2019-2-25

# Function to create a Marist-style username from user input
# Generates username in only lowercase
# Make list from returned user input?
def getName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first,last]

def makeName(name):
    return (name[0] + "." + name[1]).lower()

# Function to check strength of password
# Checks to see if password length is >8 characters
# Needs to be validated by use of both upper and lower characters
def getPass():
    passwd = input("Create a new password: ")
    while not checkPass(passwd):
        print("I sense a disturbance in the force. Your password should be a little stronger.")
        passwd = input("Create a new password: ")
    print("The force is strong in this one...")
    return passwd

def checkPass(passwd):
    if len(passwd)<8:
        return False
    if passwd.lower() == passwd:
        return False
    if passwd.upper() == passwd:
        return False
    return True
    
    
def main():

    # get user's first and last names
    name = getName()
    # TODO modify this to generate a Marist-style username
    uname = makeName(name)
    print("Your newly created username is:",f'"{uname}"')

    # ask user to create a new password
    passwd = getPass()
    
    # TODO modify this to ensure the password has at least 8 characters
    print("Account configured.")
    print("Your new email address is:",uname,"@marist.edu")

main()
