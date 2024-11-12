import pygame
import os
import random
pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1300
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Dino","Screenshot__93_-removebg-preview.png")),
           pygame.image.load(os.path.join("Dino","Screenshot__92_-removebg-preview.png"))]


JUMPING = pygame.image.load(os.path.join("Dino","IMG-20241027-WA0005[1].png"))


DUCKING = [pygame.image.load(os.path.join("Dino","IMG-20241027-WA0006[1].png")),
           pygame.image.load(os.path.join("Dino","IMG-20241027-WA0007[1].png"))]


OBSTACLE1 = pygame.image.load(os.path.join("Dino","84b72c20a9478d74c842efc08d12faf536d3fc78[1].png"))


OBSTACLE2 =  pygame.image.load(os.path.join("Dino","121154a8aad3786db95b9b1e803118b0039dce3d[1].png"))


OBSTACLE3 =  pygame.image.load(os.path.join("Dino","2b3011abc95f2183d4257a94893d42f0077c51a1[1].png"))


BIRD =    [pygame.image.load(os.path.join("Dino","IMG-20241027-WA0002[1].png")),
          pygame.image.load(os.path.join("Dino","IMG-20241027-WA0008[1].png"))]

test_surface = pygame.image.load(os.path.join("Dino","background.jpeg"))
GROUND = pygame.image.load(os.path.join("Dino","ground.png"))

UFO = pygame.image.load(os.path.join("Dino", "ufo (2).jpeg"))

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

class ufo:
    def __init__(self):
        self.x = SCREEN_WIDTH +random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = UFO
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH +random.randint(2500, 3000)
            self.y = random.randint(50, 100)
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


        


# def main():
#     global game_speed, x_pos_bg, y_pos_bg,points,font,Ufo
#     run = True
#     clock = pygame.time.Clock()
#     player = Dinosaur()
#     Ufo = ufo()
#     game_speed = 14
#     x_pos_bg = 0
#     y_pos_bg = 600
#     points = 0
#     font = pygame.font.Font('freesansbold.ttf', 20)
#     def score():
#         global points, game_speed
#         points += 1
#         if points % 100 == 0:
#             game_speed += 1

#         text = font.render("Points: " + str(points), True, (255,255,255))
#         textRect = text.get_rect()
#         textRect.center = (1000, 40)
#         SCREEN.blit(text, textRect)

#     def background():
#         global x_pos_bg, y_pos_bg
#         image_width = GROUND.get_width()
#         SCREEN.blit(GROUND, (x_pos_bg, y_pos_bg))
#         SCREEN.blit(GROUND, (image_width + x_pos_bg, y_pos_bg))
#         if x_pos_bg <= -image_width:
#             SCREEN.blit(GROUND, (image_width + x_pos_bg, y_pos_bg))
#             x_pos_bg = 0
#         x_pos_bg -= game_speed

#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

#         SCREEN.fill((0,0,0))
#         userInput = pygame.key.get_pressed()  


#         player.draw(SCREEN)
#         player.update(userInput)   

#         Ufo.draw(SCREEN)
#         Ufo.update()

#         background()
#         score()
#         clock.tick(30)
#         pygame.display.update()

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles,death_count,Ufo
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    Ufo = ufo()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 600
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = GROUND.get_width()
        SCREEN.blit(GROUND, (x_pos_bg, y_pos_bg))
        SCREEN.blit(GROUND, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(GROUND, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed



    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((0,0,0))
        userInput = pygame.key.get_pressed()
        SCREEN.blit(test_surface,(0,0))
        player.draw(SCREEN)
        player.update(userInput)

        # if len(obstacles) == 0:
        #     if random.randint(0, 2) == 0:
        #         obstacles.append(SmallCactus(SMALL_CACTUS))
        #     elif random.randint(0, 2) == 1:
        #         obstacles.append(LargeCactus(LARGE_CACTUS))
        #     elif random.randint(0, 2) == 2:
        #         obstacles.append(Bird(BIRD))

        # for obstacle in obstacles:
        #     obstacle.draw(SCREEN)
        #     obstacle.update()
        #     if player.dino_rect.colliderect(obstacle.rect):
        #         pygame.time.delay(2000)
        #         death_count += 1
        #         menu(death_count)

        background()

        Ufo.draw(SCREEN)
        Ufo.update()

        score()

        clock.tick(30)
        pygame.display.update()

               











main()
