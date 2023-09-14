import os, random, pygame
from pygame.locals import *

current_dir = os.path.dirname(__file__)

size = width, height = (1200, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1

pygame.init()

# run
running = True
# set screen size
screen = pygame.display.set_mode(size)
# set window name
pygame.display.set_caption("Car game")
# set bg color
screen.fill((60, 220, 0))

# apply changes
pygame.display.update()

# load images
car_png = os.path.join(current_dir, 'car.png')
car = pygame.image.load(car_png)
# set img location
car_loc = car.get_rect()
# set img in game location
car_loc.center = right_lane, height*0.8

# load images
car2_png = os.path.join(current_dir, 'otherCar.png')
car2 = pygame.image.load(car2_png)
# set img location
car2_loc = car.get_rect()
# set img in game location
car2_loc.center = left_lane, height*0.2

counter = 0
# while loop is for setting game do not auto stop, but after pressing "close button"
while running:
    # animate enemy vehicle
    counter += 1
    if counter == 1024:
        speed += 0.25
        counter = 0
        print('Level up', speed)
    car2_loc[1] += speed
    if car2_loc[1] > height:
        car2_loc[1] =-200
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    
    # end game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] -250 :
        print('GAME OVER! YOU LOST!')
        break
        
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2),0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2),0])
                
        # road
        pygame.draw.rect(
            screen,
            (50, 50, 50),
            (width/2-road_w/2, 0, road_w, height))

        # yellow line
        pygame.draw.rect(
            screen,
            (255, 240, 60),
            (width/2-roadmark_w/2, 0, roadmark_w, height))

        # white left line
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (width/2-road_w/2+roadmark_w*2, 0, roadmark_w, height))

        # white right line
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (width/2+road_w/2-roadmark_w*3, 0, roadmark_w, height))
            
            
    # set new in game items
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()

pygame.quit()
