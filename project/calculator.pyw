# Calculator GUI

from calc_function import *
from graphics import *

def createCanvas():
   win = GraphWin('Calc You Later!', 300, 465)
   win.setBackground('SlateGray')
   return win

def createDisplay(win):
   disp = Rectangle(Point(20,10),Point(280,90))
   disp.setFill('White')
   math = Text(Point(150,50),"Hey, can you read this?")
   disp.draw(win)
   math.draw(win)
   return math

def getLabel(i):
   labels = ['7','8','9',
             '4','5','6',
             '1','2','3',
             '.','0','DEL','=',
             '/','x','+','-',
             'M+','M-','MR','MC']
   return labels[i]

def createButtons(win):
   coords = [[20,100],[80,100],[140,100],
             [20,160],[80,160],[140,160],
             [20,220],[80,220],[140,220],
             [20,280],[80,280],[140,280],[200,280],
             [20,340],[80,340],[140,340],[200,340],
             [20,400],[80,400],[140,400],[200,400]]
   color = ['AliceBlue','AliceBlue','AliceBlue',
            'AliceBlue','AliceBlue','AliceBlue',
            'AliceBlue','AliceBlue','AliceBlue',
            'Peachpuff','AliceBlue','Peachpuff','DarkSalmon',
            'Peachpuff','Peachpuff','Peachpuff','Peachpuff',
            'Antique White','Antique White','Antique White','Antique White']
   size = [50,50,50,
           50,50,50,
           50,50,50,
           50,50,50,50,
           50,50,50,50,
           50,50,50,50]

   for i in range(len(coords)):
      x = coords[i][0]
      y = coords[i][1]
      button = Rectangle(Point(x,y),Point(x+size[i],y+size[i]))
      button.setFill(color[i])
      label = Text(Point(x+size[i]/2,y+size[i]/2),getLabel(i))
      button.draw(win)
      label.draw(win)
   return coords

def onClick(coords, mouse, equation):
   for i in range(len(coords)):
      if coords [i][0] < mouse.x < coords[i][0] + 50 and coords[i][1] < mouse.y < coords[i][1] + 50:
         key = getLabel(i)
         if key == "DEL":
            equation = equation[:len(equation) - 1]
         elif key == "=":
            equation = str(doMath(equation.split()))
         elif key in ['+','-','x','/']:
            equation = equation + ' ' + key + ' '
         #elif key == "M+":
          #  memory = equation
         #elif key == "M-":
          #  memory = memory - ' ' - key - ' '
         #elif key == "MR":
          #  equation = memory
         #elif key == "MC":
          #  memory = memory.remove(equation)
         else:
            equation = equation + key
         break
   return equation
         
def main():
   win = createCanvas()
   display = createDisplay(win)
   coords = createButtons(win)
   equation = ''   
   while True:
      mouse = win.getMouse()
      equation = onClick(coords, mouse, equation)
      display.setText(equation)
      print(equation)

main()
