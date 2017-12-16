from Enemy import *
from Bricks import *
class Bomb:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        self.bombcount = 3
        for i in range(2):
            for j in range(4):
                b.board[self.__x+i][self.__y+j]='3'
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def destroy(self,x,y):
        if bomberman.getx()==x and bomberman.gety()==y:
            bomberman.destroy()
        elif b.board[x][y]=='E':
            for e in enemy:
                if e.getx() == x and e.gety()==y:
                    e.destroy()
                    enemy.remove(e)
        elif b.board[x][y]=='/':
            for br in bricks:
                if br.getx() == x and br.gety()==y:
                    br.destroy()
                    bricks.remove(br)
        if b.board[x][y]!='#':
            for i in range(2):
                for j in range(4):
                    b.board[x+i][y+j]='e'
    def bombcountdown(self,x):
        for i in range(2):
            for j in range(4):
                b.board[self.getx()+i][self.gety()+j]=str(x)
    def explode(self):
        self.bombcount=-1
        for i in range(2):
            for j in range(4):
                b.board[self.getx()+i][self.gety()+j]='e'
        self.destroy(self.getx(),self.gety())
        self.destroy(self.getx(),self.gety()-4)
        self.destroy(self.getx(),self.gety()+4)
        self.destroy(self.getx()+2,self.gety())
        self.destroy(self.getx()-2,self.gety())
    def explodedcharchange(self,x,y):
        if b.board[x][y]=='e':
            for i in range(2):
                for j in range(4):
                    b.board[x+i][y+j]=' '
    def afterexplode(self):
        self.bombcount=0
        self.explodedcharchange(self.getx(),self.gety())
        self.explodedcharchange(self.getx(),self.gety()-4)
        self.explodedcharchange(self.getx(),self.gety()+4)
        self.explodedcharchange(self.getx()+2,self.gety())
        self.explodedcharchange(self.getx()-2,self.gety())
