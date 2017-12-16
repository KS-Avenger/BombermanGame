from Bomberman import *
from Enemy import *
from Person import *
import readchar
import os
import random
import signal
from alarmexception import *
from Bomb import *
from Bricks import *
bombcount = -2
level = 1


def alarmHandler(signum, frame) :
    raise AlarmException


def input_to(timeout=1) :
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try :
        text = readchar.readchar()
        signal.alarm(0)
        return text
    except AlarmException :
        #print("\n Prompt timeout.Continuing")
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
while level <= 3 and b.getlives() > 0 :
    if bombcount >= -1 :
        bombcount -= 1
        if bombcount >= 0 :
            bomb.bombcountdown(bombcount)
        if bombcount == -1 :
            bomb.explode()
        if bombcount == -2 :
            bomb.afterexplode()
    dir = input_to()
    #print(dir)
    if dir == 'a' :
        if bomberman.moveleft() :
            pass

    elif dir == 's' :
        if bomberman.movedown() :
            pass
    #os.system('clear')
            #b.pr()
    #        print("Lives:"+str(bomberman.lives)+"    "+ "Score:" + str(bomberman.score))

    elif dir == 'd' :
        if bomberman.moveright() :
            pass
    #os.system('clear')
            #b.pr()
    #        print("Lives:"+str(bomberman.lives)+"    "+ "Score:" + str(bomberman.score))

    elif dir == 'w' :
        if bomberman.moveup() :
            pass
    #os.system('clear')
            #b.pr()
    #        print("Lives:"+str(bomberman.lives)+"    "+ "Score:" + str(bomberman.score))

    elif dir == 'b' :
        bomb = Bomb(bomberman.getx(), bomberman.gety())
        bombcount = bomb.bombcount
    elif dir == 'q' :
        break
    lcount=0
    while lcount < level :
        i = 0
        lcount = lcount + 1
        while True :
            if(i >= len(enemy)) :
                break
            if enemy[i].isblocked() :
                i += 1
            #print("i is "+str(i))
            else :
                r = random.randint(1, 4)
                #print(r)
                if r == 1 and enemy[i].moveup() :
                    i = i + 1
                    #print("up")
                elif r == 2 and enemy[i].movedown() :
                    i = i + 1
                    #print("down")
                    #b.pr()
                elif r == 3 and enemy[i].moveleft() :
                    i = i + 1
                    #print("left")
                    #b.pr()
                elif r == 4 and enemy[i].moveright() :
                    i = i + 1
                    #print("right")
                    #b.pr()
        b.pr()
        print("Level:"+str(level))
    #print("Lives:"+str(b.lives)+"    "+ "Score:" + str(b.score))
    if enemy == [] :
        level += 1
        print("Level Up")
        if level == 2 :
            n = 6
        elif level == 3 :
            n = 8
        for k in range(n) :
            flag = 1
            while flag > 0 :
                i = random.randint(6, b.getxborder() - 4)
                j = random.randint(12, b.getyborder() - 8)
                i = i - (i % 2)
                j = j - (j % 4)
                for x in range(i, i+1) :
                    for y in range(j, j+3) :
                        if b.board[x][y] == ' ' :
                            flag = 0
            enemy.append(Enemy(i, j))
print("Final Score is :"+str(b.getscore()))
