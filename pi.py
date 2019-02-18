# pi.py

import math

def main():
    n = int(input("How many terms of Pi would you like summed?: "))
    sign = 1
    calc = 0
    for i in range(1,n*2,2):
        calc = calc+(4/i*sign)
        sign = sign*(-1)
    print(calc)
    print("And your number is exactly", math.pi-calc,"away from Pi")

main()
