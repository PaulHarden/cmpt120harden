# Calculator GUI

from calc_function import *
from graphics import *

def createCanvas():
   win = GraphWin('Calc You Later!', 300, 410,)
   win.setBackground('SlateGray')
   return win

def createDisplay(win):
   # equation = input("Enter a mathematical equation (with spaces between characters): ").split()
   # result = doMath(equation)
   # print("The result is",result)
   
   disp = Rectangle(Point(20,10),Point(280,90))
   disp.setFill('White')
   math = Text(Point(150,50),'Hey, can you read this?')
   disp.draw(win)
   math.draw(win)
   return

def createButtons(win):
   coords = [[20,100],[80,100],[140,100],
             [20,160],[80,160],[140,160],
             [20,220],[80,220],[140,220],
             [20,280],[80,280],[140,280],[200,280],
             [20,340],[80,340],[140,340],[200,340]]
   labels = ['7','8','9',
             '4','5','6',
             '1','2','3',
             '.','0','DEL','=',
             '/','x','+','-']
   color = ['AliceBlue','AliceBlue','AliceBlue',
            'AliceBlue','AliceBlue','AliceBlue',
            'AliceBlue','AliceBlue','AliceBlue',
            'Peachpuff','AliceBlue','Peachpuff','DarkSalmon',
            'Peachpuff','Peachpuff','Peachpuff','Peachpuff']
   size = [50,50,50,
           50,50,50,
           50,50,50,
           50,50,50,50,
           50,50,50,50]

   for i in range(len(coords)):
      x = coords[i][0]
      y = coords[i][1]
      button = Rectangle(Point(x,y),Point(x+size[i],y+size[i]))
      button.setFill(color[i])
      label = Text(Point(x+size[i]/2,y+size[i]/2),labels[i])
      button.draw(win)
      label.draw(win)

def main():
   win = createCanvas()
   display = createDisplay(win)
   createButtons(win)

main()
