# Calculations for Project

def doMath(equation):
   i = 0
   while hasPrec(equation):
      if equation[i] == "x" or equation[i] == "/":
         process(equation, i)
      else:
         i = i + 1
   i = 0   
   while len(equation)>1:
      if equation[i] == "+" or equation[i] == "-":
         process(equation, i)
      else:
         i = i + 1
         
   return float(equation[0])

def hasPrec(equation):
   eqstr = "".join(equation)
   if "x" in eqstr or "/" in eqstr:
      return True
   return False

   
def process(equation, i):
   if equation[i] == "x":
      result = float(equation[i - 1]) * float(equation[i + 1])
   elif equation[i] == "/":
      result = float(equation[i - 1]) / float(equation[i + 1])
   elif equation[i] == "+":
      result = float(equation[i - 1]) + float(equation[i + 1])
   elif equation[i] == "-":
      result = float(equation[i - 1]) - float(equation[i + 1])
   del equation[i - 1]
   del equation[i - 1]
   del equation[i - 1]
   equation.insert(i - 1, str(result))
