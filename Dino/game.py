import pygame
import os
import random
pygame.init()
SCREEN_HEIGHT = 800 #screen dimensions
SCREEN_WIDTH = 1300
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#assets loaded
RUN = [pygame.image.load(os.path.join("Dino","run1 (1).png")),
           pygame.image.load(os.path.join("Dino","run2 (1).png"))]
JUMP = pygame.image.load(os.path.join("Dino","jump (2) (1).png"))
DUCK = [pygame.image.load(os.path.join("Dino","crouch1 (1).png")),
          pygame.image.load(os.path.join("Dino","crouch2 (1).png"))]

SMALL_MONSTER = [pygame.image.load(os.path.join("Dino", "A.png")),
                pygame.image.load(os.path.join("Dino", "B.png")),
                pygame.image.load(os.path.join("Dino", "C.png"))]
LARGE_MONSTER = [pygame.image.load(os.path.join("Dino", "D.png")),
                pygame.image.load(os.path.join("Dino", "E.png")),
                pygame.image.load(os.path.join("Dino", "F.png"))]
BIRD =    [pygame.image.load(os.path.join("Dino","fly1 (1).png")),
          pygame.image.load(os.path.join("Dino","fly2 (1).png"))]

background_surface = pygame.image.load(os.path.join("Dino","background.jpeg"))
ROAD = pygame.image.load(os.path.join("Dino","road&border.png"))
SPACESHIP = pygame.image.load(os.path.join("Dino", "spaceship.png"))

class Player:#class to manage player's character
    X_POS = 50 #Intial positions
    Y_POS = 500
    Y_POS_DUCK =550
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCK
        self.run_img = RUN
        self.jump_img = JUMP

        self.player_duck = False
        self.player_run = True
        self.player_jump = False

        self.step_index = 0 #step for animations
        self.jump_vel=self.JUMP_VEL #defined jump
        self.image = self.run_img[0] #initial image of player
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.X_POS
        self.player_rect.y = self.Y_POS

    def update(self, userInput):
        #updated player's state
        if self.player_duck:
            self.duck()
        if self.player_run:
            self.run()
        if self.player_jump:
            self.jump()
        if self.step_index >= 10: #Reset animation index
            self.step_index = 0

#handling for jump ,duck and run
        if userInput[pygame.K_UP] and not self.player_jump:
            self.player_duck = False
            self.player_run = False
            self.player_jump = True
        elif userInput[pygame.K_DOWN] and not self.player_jump:
            self.player_duck = True
            self.player_run = False
            self.player_jump = False
        elif not (self.player_jump or userInput[pygame.K_DOWN]):
            self.player_duck = False
            self.player_run = True
            self.player_jump = False

    def duck(self):
        self.image = self.duck_img [self.step_index // 5]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.X_POS
        self.player_rect.y = self.Y_POS_DUCK
        self.step_index += 1
       
    def run(self):
        self.image = self.run_img [self.step_index // 5]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.X_POS
        self.player_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.player_jump:
            self.player_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.player_jump = False
            self.jump_vel=self.JUMP_VEL
       
    def draw(self,SCREEN): #draw the player on the screen
        SCREEN.blit(self.image, (self.player_rect.x, self.player_rect.y))

class spaceship:
    def __init__(self):
        self.x = SCREEN_WIDTH +random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = SPACESHIP
        self.width = self.image.get_width()

    def update(self):#move spaceship leftward; reset when out of screen
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH +random.randint(2500, 3000)
            self.y = random.randint(50, 100)
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
#Base obstacle class
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

class SmallMonster(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 525

class LargeMonster(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 500

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 450
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

def main():#Main loop
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles,death_count,Spaceship
    run = True
    clock = pygame.time.Clock()
    player = Player()
    Spaceship = spaceship()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 600
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():#Scoring function for game
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)
    def background():#updation of background
        global x_pos_bg, y_pos_bg
        image_width = ROAD.get_width()
        SCREEN.blit(ROAD, (x_pos_bg, y_pos_bg))
        SCREEN.blit(ROAD, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(ROAD, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((0,0,0))
        userInput = pygame.key.get_pressed()
        SCREEN.blit(background_surface,(0,0))
        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallMonster(SMALL_MONSTER))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeMonster(LARGE_MONSTER))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.player_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)
        background()
        Spaceship.draw(SCREEN)
        Spaceship.update()
        score()
        clock.tick(30)
        pygame.display.update()
def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUN[1], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()
menu(death_count=0)