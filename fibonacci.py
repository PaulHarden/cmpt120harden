# fibonacci.py

import math

def main():
    n = int(input("What step of the Fibonacci sequence would you like: "))
    old,new = 1,1
    new2 = 1
    for i in range(0,n - 2):
        new2 = old + new
        old = new
        new = new2
    print(new2,"is the",n,"th step in the Fibonacci sequence")
main()
