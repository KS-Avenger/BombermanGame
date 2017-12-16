import Board
from Board import *
class Person:
    x=0
    y=0
    def __init__(self,xi,yi):
        self.__x=xi
        self.__y=yi
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def setx(self,x):
        self.__x=x
    def sety(self,y):
        self.__y=y
    def checkup(self):
        if b.board[self.getx()-2][self.gety()] == ' ' or b.board[self.getx()][self.gety()] == 'e':
            return True
        else:
            return False
    def checkdown(self):
        if b.board[self.getx()+2][self.gety()] == ' ' or b.board[self.getx()][self.gety()] == 'e':
            return True
        else:
            return False
    def checkleft(self):
        if b.board[self.getx()][self.gety()-4] == ' ' or b.board[self.getx()][self.gety()] == 'e':
            return True
        else:
            return False
    def checkright(self):
        if b.board[self.getx()][self.gety()+4] == ' ' or b.board[self.getx()][self.gety()] == 'e':
            return True
        else:
            return False
