# Calculator GUI

from calc_function import *

def main():
   equation = input("Enter a mathematical equation (with spaces between characters): ").split()
   result = doMath(equation)
   print("The result is",result)
   
main()
