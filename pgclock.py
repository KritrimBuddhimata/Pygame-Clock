#Clock Example in pygame
#Modules used

import os, sys, pygame
from pygame.locals import *
import datetime

class item:

    def __init__(self,imagename,colorkey,left,top):
        self.img = pygame.image.load(imagename).convert()
        if colorkey == -1:
            ckey = self.img.get_at((0,0))
            self.img.set_colorkey(ckey, RLEACCEL)
        self.rect = self.img.get_rect()
        self.left = left
        self.top = top
        self.width = self.rect.width
        self.height = self.rect.height
        self.center = self.rect.center

    def draw(self):
        screen.blit(self.img,(self.left, self.top))

    def setaxis(self,axis):
        self.axis = axis

    def drawrot(self,axis,angle):
        #Create new rotated image: preserve original
        self.newimg = pygame.transform.rotate(self.img,angle).convert()
        self.newrect = self.newimg.get_rect()
        #Now center the new rectangle to the rotation axis
        self.newrect.left = axis[0]-(self.newrect.w/2)
        self.newrect.top = axis[1]-(self.newrect.h/2)
        screen.blit(self.newimg,(self.newrect.left, self.newrect.top))

#setup screen size and background image

size = width, height = 200, 244
screen = pygame.display.set_mode(size)
pygame.init()

#load clock face as background        
bg = item("clock-face.jpg",0,0,0)
bg.setaxis((bg.width/2,95))

#load and place clock hands
#the hand images rotate around their own central axis because
#almost one half of the image is set to transparent
longhand = item("clockhand-long.bmp",-1,90,23)
shorthand = item("clockhand-short.bmp",-1,90,40)
