import random
from Bomberman import *
class Brick:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        for i in range(2):
            for j in range(4):
                b.board[self.__x+i][self.__y+j]='/'
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def destroy(self):
        for i in range(2):
            for j in range(4):
                b.board[self.getx()+i][self.gety()+j]=' '
        b.setscore(b.getscore()+50)
bricks=[]
for k in range(5):
    flag=1
    while flag>0:
        i=random.randint(6,b.getxborder()-4)
        j=random.randint(12,b.getyborder()-8)
        i= i - (i%2)
        j= j - (j%4)
        for x in range(i,i+1):
            for y in range(j,j+3):
                if b.board[x][y] == ' ' :
                    flag=0
    bricks.append(Brick(i,j))
