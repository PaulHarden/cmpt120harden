# Calculator GUI

from calc_function import *
from graphics import *

class Calculator:

    def __init__(self):
        self.win = GraphWin('Calc You Later!', 300, 465)
        self.win.setBackground('SlateGray')
        self.display = Display(self.win)
        self.keypad = Keypad(self.win)

    def run(self):
        while True:
            key = self.keypad.getKeyPressed()
            print(key)
            result = self.engine.addKeyPressed()
            if result == "quit":
                break
        self.display.setText(result)


class Display:
    
    def __init__(self, win):
        self.display = self.createDisplay(win)

    def createDisplay(self, win):
        disp = Rectangle(Point(20,10),Point(280,90))
        disp.setFill('White')
        math = Text(Point(150,50),"Hey, can you read this?")
        disp.draw(win)
        math.draw(win)
        return math


class Button:

    def __init__(self, win, coords, size, color, label):
        self.coords = coords
        self.size = size
        self.button = Rectangle(Point(coords[0],coords[1]),Point(coords[0]+size,coords[1]+size))
        self.button.setFill(color)
        self.button.draw(win)
        self.label = Text(Point(coords[0]+size/2,coords[1]+size/2),label)
        self.label.draw(win)
        

    def getLabel(self):
        return self.label.getText()

    def isPressed(self, point):
        if self.coords[0] <= point.getX() <= self.coords[0] + self.size and \
           self.coords[1] <= point.getY() <= self.coords[1] + self.size:
            return True
        return False
        
        

class Keypad:

    def __init__(self, win):
        self.buttons = self.createButtons(win)
        self.win = win

    def getKeyPressed(self):
            p = self.win.getMouse()
            return self.checkKey(p)

    def checkKey(self, point):
        for b in self.buttons:
            if b.isPressed(point):
                return b.getLabel()
    

    def createButtons(self, win):
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
        labels = ['7','8','9',
                  '4','5','6',
                  '1','2','3',
                  '.','0','DEL','=',
                  '/','x','+','-',
                  'M+','M-','MR','MC']
        buttons = []
        for i in range(len(coords)):
            button = Button(win, coords[i], size[i], color[i], labels[i])
            buttons.append(Button)
        return buttons
        

          

    def onClick(coords, mouse, equation, memory):
        for i in range(len(coords)):
         if coords [i][0] < mouse.x < coords[i][0] + 50 and coords[i][1] < mouse.y < coords[i][1] + 50:
            key = getLabel(i)
            if key == "DEL":
               equation = equation[:len(equation) - 1]
            elif key == "=":
               equation = str(doMath(equation.split()))
            elif key in ['+','-','x','/']:
               equation = equation + ' ' + key + ' '
            elif key == "M+":
               memory = memory + doMath(equation.split())
            elif key == "M-":
               memory = memory - doMath(equation.split())
            elif key == "MR":
               equation = equation + str(memory)
            elif key == "MC":
               memory = 0
            else:
               equation = equation + key
            break
        return equation, memory

def main():
    calc = Calculator()
    calc.run()

main()
