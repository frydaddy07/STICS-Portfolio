'''
Created on Apr 5, 2017

@author: Nathanael Mathieu, Avi Stein, Kevin McMorrow, Jesse Galganov

'''
from ParticleClass import Particle
def x_dist(Particle1, Particle2):
        return abs(Particle1.getXPos() - Particle2.getXPos())

def y_dist(Particle1, Particle2):
        return abs(Particle1.getYPos() - Particle2.getYPos())
    
def signOf(value):
    if value != 0:
        return value / abs(value)  # gets the sign of the value
    else:  # or returns 1 when no sign is present (value = 0)
        return 1
    

maxXPos = 20
maxYPos = 20
numberOfRuns = 4


def update(ben, jerry):
    if (x_dist(ben, jerry) and y_dist(ben, jerry)) == 0:
        print("ERROR: BEN AND JERRY CANNOT OCCUPY SAME SPACE")

    ben_current_xVel = ben.getXVel()
    ben_current_yVel = ben.getYVel()
    jerry_current_xVel = jerry.getXVel()
    jerry_current_yVel = jerry.getYVel()

    ben_current_xPos = ben.getXPos()
    ben_current_yPos = ben.getYPos()
    jerry_current_xPos = jerry.getXPos()
    jerry_current_yPos = jerry.getYPos()

    # change velocity in x proportional to force derived by LJ

    if x_dist(ben, jerry) == 1:
        ben_current_xVel += -4 * signOf(jerry_current_xVel)  # updates location by multiplying the sign of Jerry's velocity with -4, forcing it in the opposite direction
        jerry_current_xVel += -4 * signOf(ben_current_xVel)  # updates location by multiplying the sign of Ben's velocity with -4, forcing it in the opposite direction
        ben.setVel([ben_current_xVel, ben_current_yVel])
        jerry.setVel([jerry_current_xVel, jerry_current_yVel])

    elif x_dist(ben, jerry) == 3:
        ben_current_xVel += 1 * signOf(jerry_current_xVel)
        jerry_current_xVel += 1 * signOf(ben_current_xVel)
        ben.setVel([ben_current_xVel, ben_current_yVel])
        jerry.setVel([jerry_current_xVel, jerry_current_yVel])

    # at 2 - no repulsion (ideal distance), at 4+ - too far to interact
    else:
        print("no X repulsion")

    # change velocity in y proportional to force derived by LJ

    if y_dist(ben, jerry) == 1:
        ben_current_yVel += -4 * signOf(jerry_current_yVel)
        jerry_current_yVel += -4 * signOf(ben_current_yVel)
        ben.setVel([ben_current_xVel, ben_current_yVel])
        jerry.setVel([jerry_current_xVel, jerry_current_yVel])


    elif y_dist(ben, jerry) == 3:
        ben_current_yVel += signOf(jerry_current_yVel)
        jerry_current_yVel += signOf(ben_current_yVel)
        ben.setVel([ben_current_xVel, ben_current_yVel])
        jerry.setVel([jerry_current_xVel, jerry_current_yVel])

    # at 2 - no repulsion (ideal distance), at 4+ - too far to interact
    else:
        print("no Y repulsion")
        
    if(ben_current_xPos + ben_current_xVel) > maxXPos:  # if ben's position + velocity is out of bounds in the positive direction
        ben_current_xPos = 2 * maxXPos - (ben_current_xPos + ben_current_xVel)  # set his position to where he rebounds to
        ben.hitSideWall()  # set X velocity to be negative
    elif(ben_current_xPos + ben_current_xVel) < 0:  # if ben's position+velocity is out of bounds in the negative direction
        ben_current_xPos = 0 - ben_current_xPos - ben_current_xVel  # set position to the location he rebounds to
        ben.hitSideWall()  # set his velocity to be the opposite of what it was
    else:
        ben_current_xPos += ben_current_xVel
    if(ben_current_yPos + ben_current_yVel) > maxYPos:
        ben_current_yPos = 2 * maxYPos - (ben_current_yPos + ben_current_yVel)
        ben.hitTopOrBottomWall()
    elif(ben_current_yPos + ben_current_yVel) < 0:
        ben_current_yPos = 0 - ben_current_yPos - ben_current_yVel
        ben.hitTopOrBottomWall()
    else:
        ben_current_yPos += ben_current_yVel
        
    ben.setPos([ben_current_xPos, ben_current_yPos])



    if (jerry_current_xPos + jerry_current_xVel) > maxXPos:
        jerry_current_xPos = 2 * maxXPos - (jerry_current_xPos + jerry_current_xVel)
        jerry.hitSideWall()
    elif (jerry_current_xPos + jerry_current_xVel) < 0:
        jerry_current_xPos = 0 - jerry_current_xPos - jerry_current_xVel
        jerry.hitSideWall()
    else:
        jerry_current_xPos += jerry_current_xVel
    if (jerry_current_yPos + jerry_current_yVel) > maxYPos:
        jerry_current_yPos = 2 * maxYPos - (jerry_current_yPos + jerry_current_yVel)
        jerry.hitTopOrBottomWall()
    elif (jerry_current_yPos + jerry_current_yVel) < 0:
        jerry_current_yPos = 0 - jerry_current_yPos - jerry_current_yVel
        jerry.hitTopOrBottomWall()
    else:
        jerry_current_yPos += jerry_current_yVel
    
    jerry.setPos([jerry_current_xPos, jerry_current_yPos])

def main():

    # grid is 20x20 - positions range from (0,0) to (20,20)
    # 1 unit away - repulse 4 unit/sec
    # 2 unit away - keep going, no change
    # 3 unit away - attract slightly - 1unit/sec
    # 4-7 unit away - continue, no change

    # jerry_pos = input("Please enter a position: ") # prompt input for positions and velocities
    # they must be placed on the 20 x 20 grid and not occupy the same position

    ben = Particle(0, 0, 1, 1)  # sets ben's position at [0, 0] and velocity at [1, 1]
    jerry = Particle(1, 1, 0, 0)

    
    old_x_dist = x_dist(ben, jerry)
    old_y_dist = y_dist(ben, jerry)
    old_jerryPos = jerry.getPos()
    old_jerryVel = jerry.getVel()
    old_benPos = ben.getPos()
    old_benVel = ben.getVel()

    
    
    for i in range(1, numberOfRuns):
        print("run {}".format(i))
        update(ben, jerry)

    print("x distance {0} to {1}".format(old_x_dist, x_dist(ben, jerry)))
    print("y distance {0} to {1}".format(old_y_dist, y_dist(ben, jerry)))
    print("jerry pos {0} to {1}".format(old_jerryPos, jerry.getPos()))
    print("jerry vel {0} to {1}".format(old_jerryVel, jerry.getVel()))
    print("ben pos {0} to {1}".format(old_benPos, ben.getPos()))
    print("ben vel {0} to {1}".format(old_benVel, jerry.getVel()))

main()
