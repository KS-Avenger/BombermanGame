import sys
import os
import colorama
from colorama import Fore,Style,Back#,init
#init(autoreset=True)
class Board:
    #os.system('clear')
    xborder=0
    yborder=0
    board=[]
    def __init__(self,xi,yi):
        border=['#' for y in range(82)]
        self.__xborder=xi
        self.__yborder=yi
        self.board=[[' ' for y in range(yi)] for x in range(xi)]
        self.__lives=3
        self.__score=0
        for x in range(self.getxborder()):
            if x<2:
                self.board[x]=['#' for y in range(yi)]
            elif x>=xi-2:
                self.board[x]=['#' for y in range(yi)]
            elif x%4 >=2 :
                for y in range(self.getyborder()):
                    if y<4 :
                        self.board[x][y]='#'
                    elif y> yi-5:
                        self.board[x][y]='#'
            elif x%4 <2:
                for y in range(self.getyborder()):
                    if y<4 :
                        self.board[x][y]='#'
                    elif y> yi-5:
                        self.board[x][y]='#'
                    elif y % 8 < 4 :
                        self.board[x][y]='#'
    def getxborder(self):
        return self.__xborder
    def getyborder(self):
        return self.__yborder
    def getscore(self):
        return self.__score
    def setscore(self,x):
        self.__score = x
    def getlives(self):
        return self.__lives
    def declives(self):
        self.__lives = self.getlives() - 1
    def pr(self):
        os.system('clear')
        for x in range(self.getxborder()):
            for y in range(self.getyborder()):
                if self.board[x][y] == 'E' :
                    print('E' ,end='')
                    #print(Fore.RESET,end='')
                elif self.board[x][y] == 'B' :
                    print('B' ,end='')
                    #print(Fore.RESET,end='')
                elif self.board[x][y] == '/' :
                    print('/',end='')
                    #print(Fore.RESET,end='')
                elif self.board[x][y] == 'e' :
                    print(Back.RED + 'e',end='')
                    print(Back.RESET,end='')
                else:
                    #print(Style.BRIGHT + self.board[x][y],end='')
                    #print(Style.RESET_ALL,end='')
                    print(self.board[x][y],end='')
            print()
        print("Lives :"+str(self.getlives())+"    "+ "Score:" + str(self.getscore()),end = '    ')
b=Board(42,84)
