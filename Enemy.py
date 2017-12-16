from Bomberman import *
import random
class Enemy(Person):
    def __init__(self,xi,yi):
        Person.__init__(self,xi,yi)
        for x in range(2):
            for y in range(4):
                b.board[xi+x][yi+y]='E'
    def checkup(self):
        if super().checkup() or b.board[self.getx()-2][self.gety()] == 'B' :
            return True
        else:
            return False
    def checkdown(self):
        if super().checkdown() or b.board[self.getx()+2][self.gety()] == 'B' :
            return True
        else:
            return False
    def checkleft(self):
        if super().checkleft() or b.board[self.getx()][self.gety()-4] == 'B' :
            return True
        else:
            return False
    def checkright(self):
        if super().checkright() or b.board[self.getx()][self.gety()+4] == 'B' :
            return True
        else:
            return False

    def isblocked(self):
        if self.checkup() or self.checkdown() or self.checkleft or self.checkright() :
            return False
        else:
            return True
    def moveup(self):
        if b.board[self.getx()-2][self.gety()]=='B' :
            bomberman.destroy()
        if self.checkup() :
            for x in range(2):
                for y in range(4):
                    b.board[self.getx()+x][self.gety()+y]=' '
                    b.board[self.getx() - 2 +x][ self.gety()+y] = 'E'
            self.setx(self.getx()-2)
            return True
        else:
            return False
    def movedown(self):
        if b.board[self.getx()+2][self.gety()]=='B' :
            bomberman.destroy()
        if self.checkdown() :
            for x in range(2):
                for y in range(4):
                    b.board[self.getx() + x][self.gety() + y]=' '
                    b.board[self.getx() + 2 +x][ self.gety() + y] = 'E'
            self.setx(self.getx()+2)
            return True
        else:
            return False

    def moveleft(self):
        if b.board[self.getx()][self.gety()-4]=='B' :
            bomberman.destroy()
        if self.checkleft() :
            for x in range(2):
                for y in range(4):
                    b.board[self.getx()+x][self.gety()+y]=' '
                    b.board[self.getx()+x][ self.gety() + y -4] = 'E'
            self.sety(self.gety()-4)
            if b.board[self.getx()][self.gety()-4]=='B' :
                bomberman.destroy()
            return True
        else:
            return False

    def moveright(self):
        if b.board[self.getx()][self.gety()+4]=='B' :
            bomberman.destroy()
        if self.checkright() :
            for x in range(2):
                for y in range(4):
                    b.board[self.getx()+x][self.gety()+y]=' '
                    b.board[self.getx()+x][ self.gety() + y +4] = 'E'
            self.sety(self.gety()+4)
            return True
        else:
            return False
    def destroy(self):
        for i in range(2):
            for j in range(4):
                b.board[self.getx()+i][self.gety()+j]=' '
        #increase score 100
        b.setscore(b.getscore() +100)
enemy=[]
for k in range(4):
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
    enemy.append(Enemy(i,j))
