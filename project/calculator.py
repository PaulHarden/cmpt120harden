# Calculator GUI

import cal_function

def main():
   equation = input("Enter a mathematical equation (with spaces between characters): ").split()
   result = doMath(equation)
   print("The result is",result)
   
main()
