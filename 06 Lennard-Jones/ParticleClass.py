'''
Created on Apr 5, 2017

@author: 
'''

class Particle(object):
    '''
    classdocs
    '''
    particleCount = 0

    def __init__(self, xPos, yPos, xVel, yVel): 
        self.xPos = xPos
        self.yPos = yPos
        self.xVel = xVel
        self.yVel = yVel
        Particle.particleCount += 1
    # Get Commands:
    def getPos(self):  # returns the object's positions in a 2 item list
        return [self.xPos, self.yPos]
    def getXPos(self):  # returns the object's x position
        return self.xPos
    def getYPos(self):  # returns the object's Y position
        return self.yPos
    def getVel(self):  # returns the object's velocities in a 2 item list
        return [self.xVel, self.yVel]
    def getXVel(self):  # returns the object's X velocity
        return self.xVel
    def getYVel(self):  # returns the object's Y velocity
        return self.yVel
    
    # Set Commands
    def setXPos(self, xPos):  # sets the object's x position from a number value
        self.xPos = xPos
    def setYPos(self, yPos):  # sets the object's y position from a number value
        self.yPos = yPos
    def setXVel(self, xVel):  # sets the object's x velocity from a number value
        self.xVel = xVel
    def setYVel(self, yVel):  # sets the object's y velocities from a number value
        self.yVel = yVel
    def setPos(self, pos):  # sets the object's position from a 2(+) item list
        self.xPos = pos[0]
        self.yPos = pos[1]
    def setVel(self, vel):  # sets the object's velocity from a 2(+) item list
        self.xVel = vel[0]
        self.yVel = vel[1]
    
    # Other Commands
    def hitSideWall(self):  # sets the object's velocities be be the opposite sign
        self.xVel = -self.xVel
    def hitTopOrBottomWall(self):  # sets the object's velocities be be the opposite sign
        self.yVel = -self.yVel
    def getNumberOfParticles(self):  # returns the number of constructed particle objects
        return self.particleCount
