import pygame
import os

pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Dino","1.png")),
           pygame.image.load(os.path.join("Dino","2.png"))]


JUMPING = pygame.image.load(os.path.join("Dino","IMG-20241027-WA0005[1].png"))


DUCKING = [pygame.image.load(os.path.join("Dino","IMG-20241027-WA0006[1].png")),
           pygame.image.load(os.path.join("Dino","IMG-20241027-WA0007[1].png"))]


OBSTACLE1 = pygame.image.load(os.path.join("Dino","84b72c20a9478d74c842efc08d12faf536d3fc78[1].png"))


OBSTACLE2 =  pygame.image.load(os.path.join("Dino","121154a8aad3786db95b9b1e803118b0039dce3d[1].png"))


OBSTACLE3 =  pygame.image.load(os.path.join("Dino","2b3011abc95f2183d4257a94893d42f0077c51a1[1].png"))


BIRD =    [pygame.image.load(os.path.join("Dino","IMG-20241027-WA0002[1].png")),
          pygame.image.load(os.path.join("Dino","IMG-20241027-WA0008[1].png"))]


GROUND = pygame.image.load(os.path.join("Dino","ground.png"))


BG1 = pygame.image.load(os.path.join("Dino","plx-1.png"))


BG2 = pygame.image.load(os.path.join("Dino","plx-2.png"))

BG3 = pygame.image.load(os.path.join("Dino","plx-3.png"))

BG4 = pygame.image.load(os.path.join("Dino","plx-4.png"))

BG5 = pygame.image.load(os.path.join("Dino","plx-5.png"))

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK =340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS


    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img [self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1
        pass

    def run(self):
        self.image = self.run_img [self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1


    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
        pass
        


    def draw(self,SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


        

def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255,255,255))
        userInput = pygame.key.get_pressed()  


        player.draw(SCREEN)
        player.update(userInput)   

        clock.tick(30)
        pygame.display.update()

               











main()

