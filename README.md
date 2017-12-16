# Bomberman Game in Terminal

## How to execute:
      Command for executing the game is ipython3 play.py

## The game contains 4 kinds of objects :
      - Walls(Undestroyable)
      - Bricks(Destroyable)
      - Enemies(Destroyable)
      - Bomberman(Destroyable)

## Movements:
-    You can control the moments of bomberman
    -    'a' - moveleft
    -    's' - movedown
    -    'd' - moveright
    -    'w' - moveup
    -    'q' - Exit
## Colors :
-    White - Walls
-    Green - Bomberman
-    Red   - Enemies
-    Yellow- Bricks

## Bomb:
- The bomb explodes 4 frames after its placement by the Bomberman.
- The Bomb explosion has its effect for 1 block from it.
- The Bomb has its effect on only bricks,Bomberman,Enemies.

## Death:

- If Bomberman meets an Enemie then the Bomberman lives decreases.
- If Bomberman lives becomes zero then the game is over.


## Levels:
      There are three levels.
      Initially it is in first level.
      If in any certain level the bomberman killed all the enemies then game will got to its upper level.
      As increase your level , No. of enemies and the max steps an Enemie can take in one sec increases .

## Score:
  If you kill an Enemie then your score increases by 100.
  If you destroy a brick then your score increases by 50.
