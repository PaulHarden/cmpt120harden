# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Paul Harden
# Created: 2019-2-25

# Function to create a Marist-style username from user input
# Generates username in only lowercase
def makeName(first, last):
    uname = first[0] + "." + last[:7]
    return uname.lower()

# Function to check strength of password
# Checks to see if password length is >8 characters
# Needs to be validated by use of both upper and lower characters
def passCheck():
    passwd = input("Create a new password: ")
    while len(passwd)<8:  
        print("I sense a disturbance in the force. Your password should contain 8 or more characters.")
        passwd = input("Create a new password: ")
    ##while len(passwd)<8:  
        ##print("I sense a disturbance in the force. Your password could be better...")
        ##passwd = input("Create a new password: ")
    
def main():

    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    # TODO modify this to generate a Marist-style username
    uname = makeName(first, last)
    print("Your newly created username is:",f'"{uname}"')

    # ask user to create a new password
    passwd = passCheck()
    
    # TODO modify this to ensure the password has at least 8 characters
    print("The force is strong in this one...")
    print("Account configured.")
    print("Your new email address is:",uname,"@marist.edu")

main()
