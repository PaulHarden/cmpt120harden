# Calculations for Project

def doMath(equation):
   i = 0
   while len(equation)>1 and hasProdDiv(equation, i):
      if equation[i] == "*":
         equation = process(equation, i)
      if equation[i] == "/":
         equation = process(equation, i)
      if equation[i] == "+":
         equation = process(equation, i)
      if equation[i] == "-":
         equation = process(equation, i)

def process(equation, i):
   for i in range(equation):
      op1 = i - 1
      op2 = i + 1
      result = return [op1 * op2]
   
def main():
   equation = input("Enter a mathematical equation (with spaces between characters): ").split()
   result = doMath(equation)
   print("The result is",result)
   
main()
