import os, random, pygame
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox

class CarGame:
    def __init__(self):
        self.current_dir = os.path.dirname(__file__)

        self.size = self.width, self.height = (1200, 800)
        self.road_w = int(self.width / 1.6)
        self.roadmark_w = int(self.width / 80)
        self.right_lane = self.width / 2 + self.road_w / 4
        self.left_lane = self.width / 2 - self.road_w / 4
        self.speed = 1

        self.root = tk.Tk()
        self.root.withdraw()

        pygame.init()

        self.running = True
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Car game")
        self.screen.fill((60, 220, 0))
        pygame.display.update()

        self.car_png = os.path.join(self.current_dir, 'car.png')
        self.car = pygame.image.load(self.car_png)
        self.car_loc = self.car.get_rect()
        self.car_loc.center = self.right_lane, self.height * 0.8

        self.car2_png = os.path.join(self.current_dir, 'otherCar.png')
        self.car2 = pygame.image.load(self.car2_png)
        self.car2_loc = self.car.get_rect()
        self.car2_loc.center = self.left_lane, self.height * 0.2

        self.counter = 0

    def on_yes(self):
        print("Wybrano opcję 'Tak'")
        self.root.quit()

    def on_no(self):
        print("Wybrano opcję 'Nie'")
        self.root.quit()

    def check_collision(self):
        if self.car_loc[0] == self.car2_loc[0] and self.car2_loc[1] > self.car_loc[1] - 250:
            print('GAME OVER! YOU LOST!')
            self.speed = 0
            messagebox.showinfo("Game Over", "You crashed the car!")
            response = messagebox.askquestion("Choice", "Do you like to continue?", icon='question')

            if response == 'yes':
                self.on_yes()
            else:
                self.on_no()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == KEYDOWN:
                if event.key in [K_a, K_LEFT]:
                    self.car_loc = self.car_loc.move([-int(self.road_w / 2), 0])
                if event.key in [K_d, K_RIGHT]:
                    self.car_loc = self.car_loc.move([int(self.road_w / 2), 0])

    def run(self):
        while self.running:
            self.counter += 1
            if self.counter == 1024:
                self.speed += 0.25
                self.counter = 0
                print('Level up', self.speed)
            self.car2_loc[1] += self.speed
            if self.car2_loc[1] > self.height:
                self.car2_loc[1] = -200
                if random.randint(0, 1) == 0:
                    self.car2_loc.center = self.right_lane, -200
                else:
                    self.car2_loc.center = self.left_lane, -200

            self.check_collision()
            self.handle_events()

            self.screen.fill((60, 220, 0))

            pygame.draw.rect(
                self.screen,
                (50, 50, 50),
                (self.width / 2 - self.road_w / 2, 0, self.road_w, self.height))

            pygame.draw.rect(
                self.screen,
                (255, 240, 60),
                (self.width / 2 - self.roadmark_w / 2, 0, self.roadmark_w, self.height))

            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                (self.width / 2 - self.road_w / 2 + self.roadmark_w * 2, 0, self.roadmark_w, self.height))

            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                (self.width / 2 + self.road_w / 2 - self.roadmark_w * 3, 0, self.roadmark_w, self.height))

            self.screen.blit(self.car, self.car_loc)
            self.screen.blit(self.car2, self.car2_loc)

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = CarGame()
    game.run()
