import numpy as np
import cv2 as cv
import random

# general parameters
width = 900
height = 600
n_trees = 30
ground_level = height-100

# colours
# green, light_green, brown = (40, 185, 40), (25, 220, 0), (30, 65, 155)

# blank image
bg = np.zeros((height, width, 3), dtype=np.uint8)

# draw background
cv.rectangle(bg, (width, 0), (0, ground_level), (255, 225, 95), -1)


# ***************


class Tree:
    def __init__(self, image):
        self.img = image
        self.loc = int(np.random.choice(range(900),1))
        self.ht = int(np.random.choice(range(200,350),1))
        self.radius = 50
        self.scale = np.random.choice(np.linspace(0.5,2.5,num=8),1)
        
    def generate_colours(self):
        green=(0, random.randint(130,200),0)
        light_green=(35, random.randint(200,250),35)
        brown = random.choice([(2,30,85),(5,55,120),(0,70,140)])
        return green, light_green, brown
    
    def draw(self):
        small_radius = int(self.radius*self.scale-20*self.scale) 
        light_green_radious = 10*self.scale
        green, light_green, brown = self.generate_colours()
        
        # leaf - shadows
        cv.circle(self.img, (self.loc, ground_level - self.ht),int(self.radius * self.scale), green, -1)
        cv.circle(self.img, (self.loc-int(45*self.scale), ground_level - self.ht + small_radius), small_radius, green, -1)
        cv.circle(self.img, (self.loc+int(45*self.scale), ground_level - self.ht + small_radius), small_radius, green, -1)
        
        ###
        # Dodawanie głębi obrazkowi
        
        # trunk
        cv.line(self.img, (self.loc, ground_level), (self.loc, ground_level - self.ht), brown, int(20*self.scale))
        
        # branch
        cv.line(self.img, (self.loc, ground_level - self.ht + int(75*self.scale)), (self.loc+int(45*self.scale), ground_level - self.ht + small_radius), brown, int(5*self.scale))
        cv.line(self.img, (self.loc, ground_level - self.ht + int(75*self.scale)), (self.loc-int(45*self.scale), ground_level - self.ht + small_radius), brown, int(5*self.scale))
        
        ###
        
        # leaf - highlights
        cv.circle(self.img, (self.loc,ground_level-self.ht), int(self.radius*self.scale-light_green_radious), light_green, -1)
        cv.circle(self.img, (self.loc-int(45*self.scale),ground_level-self.ht+small_radius),small_radius-int(light_green_radious),light_green, -1)
        cv.circle(self.img, (self.loc+int(45*self.scale), ground_level - self.ht + small_radius), small_radius-int(light_green_radious), light_green, -1)
           
        # floor on top
        cv.rectangle(bg, (width, ground_level), (0, height), (70,180,75), -1)
        
        return self.img
# ***************


# display image
for i in range(n_trees):
    img = Tree(bg).draw()


cv.imshow('forest of objects', img)

cv.waitKey(0)
cv.destroyAllWindows()
