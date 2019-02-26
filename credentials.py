# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Paul Harden
# Created: 2019-2-25

def makeName(first, last):
    uname = first[0] + "." + last[:7]
    return uname

def main():

    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    # TODO modify this to generate a Marist-style username
    uname = makeName(first, last)
    print("Your newly created username is:",f'"{uname}"')

    # ask user to create a new password
    passwd = input("Create a new password: ")

    # TODO modify this to ensure the password has at least 8 characters
    while len(passwd)<8:  
        print("I sense a disturbance in the force. Your password could be better...")
        passwd = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Account configured.")
    print("Your new email address is:",uname,"@marist.edu")

main()
