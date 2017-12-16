from Person import *
class Bomberman(Person):
    def __init__(self,xi,yi):
        Person.__init__(self,xi,yi)

        for x in range(2):
            for y in range(4):
                b.board[xi+x][yi+y]='B'
        #print(1)
    def changelocation(self,x,y):
        if b.board[self.getx()][self.gety()]!=' ' and b.board[self.getx()][self.gety()] !='B':
            for i in range(2):
                for j in range(4):
                    b.board[x+i][y+j]='B'
        else:
            for i in range(2):
                for j in range(4):
                    b.board[self.getx()+i][self.gety()+j]=' '
                    b.board[x+i][y+j]='B'
        self.setx(x)
        self.sety(y)
    def checkup(self):
        if super().checkup() or b.board[self.getx()-2][self.gety()] == 'E' :
            return True
        else:
            return False
    def checkdown(self):
        if super().checkdown() or b.board[self.getx()+2][self.gety()] == 'E' :
            return True
        else:
            return False
    def checkleft(self):
        if super().checkleft() or b.board[self.getx()][self.gety()-4] == 'E' :
            return True
        else:
            return False
    def checkright(self):
        if super().checkright() or b.board[self.getx()][self.gety()+4] == 'E' :
            return True
        else:
            return False

    def moveup(self):
        if b.board[self.getx()-2][self.gety()]=='E' :
            bomberman.destroy()
        if self.checkup() :
            self.changelocation(self.getx()-2,self.gety())
            return True
        return False
    def movedown(self):
        if b.board[self.getx()+2][self.gety()]=='E' :
            bomberman.destroy()
        if self.checkdown() :
            x=self.getx()
            y=self.gety()
            self.changelocation( x+2 , y )
            return True
        return False
    def moveleft(self):
        if b.board[self.getx()][self.gety()-4]=='E' :
            bomberman.destroy()
        if self.checkleft() :
            bomberman.changelocation(self.getx(),self.gety()-4)
            return True
        return False
    def moveright(self):
        if b.board[self.getx()][self.gety()+4]=='E' :
            bomberman.destroy()
        if self.checkright() :
            bomberman.changelocation(self.getx(),self.gety()+4)
            return True
        return False
    def destroy(self):
        b.declives()
        if self.getx()==2 and self.gety()==4 :
            self.changelocation(2,8)
        else:
            self.changelocation(2,4)
bomberman=Bomberman(2,4)
