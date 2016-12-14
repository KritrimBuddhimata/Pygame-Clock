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

#Assign Font
black = 0,0,0
white = 255,255,255
font = pygame.font.Font(None, 40)          

while 1:

    for event in pygame.event.get():
        if event.type == QUIT:
           sys.exit(0)

    #redraw the background to clear the screen
    bg.draw()

    dt=str(datetime.datetime.today())
    hr = float(dt[11:13])
    min = float(dt[14:16])
    sec = float(dt[17:19])
    time = dt[11:19]

    second = -360.0/60*sec +1
    minute = -360.0/60*min +1
    hour = hr % 12
    hour1 = -360.0/12*hour +1
    offset = 360.0/12/60*min
    hour = hour1-offset
    shorthand.drawrot(bg.axis,hour)
    longhand.drawrot(bg.axis,minute)
    fontimg = font.render(time,1,white)
    screen.blit(fontimg, (47,198))
    fontimg = font.render(time,1,black)
    screen.blit(fontimg, (45,196))

    pygame.display.update() 
    pygame.time.delay(500)