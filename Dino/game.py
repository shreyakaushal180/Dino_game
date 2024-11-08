import pygame
import os
import random
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

CLOUD = pygame.image.load(os.path.join("Dino", "Cloud.png"))
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

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH +random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH +random.randint(2500, 3000)
            self.y = random.randint(50, 100)
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


        


def main():
    global game_speed, x_pos_bg, y_pos_bg,points,font
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 600
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
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

        SCREEN.fill((255,255,255))
        userInput = pygame.key.get_pressed()  


        player.draw(SCREEN)
        player.update(userInput)   

        cloud.draw(SCREEN)
        cloud.update()

        background()
        score()
        clock.tick(30)
        pygame.display.update()
<<<<<<< HEAD
#preload obstacles
=======
               

#                extends Node

# #preload obstacles
>>>>>>> 628090bbc5a7bbcd93c1d958d771808ed2c567d6
# var stump_scene = preload("res://scenes/stump.tscn")
# var rock_scene = preload("res://scenes/rock.tscn")
# var barrel_scene = preload("res://scenes/barrel.tscn")
# var bird_scene = preload("res://scenes/bird.tscn")
# var obstacle_types := [stump_scene, rock_scene, barrel_scene]
# var obstacles : Array
# var bird_heights := [200, 390]

# #game variables
# const DINO_START_POS := Vector2i(150, 485)
# const CAM_START_POS := Vector2i(576, 324)
# var difficulty
# const MAX_DIFFICULTY : int = 2
# var score : int
# const SCORE_MODIFIER : int = 10
# var high_score : int
# var speed : float
# const START_SPEED : float = 10.0
# const MAX_SPEED : int = 25
# const SPEED_MODIFIER : int = 5000
# var screen_size : Vector2i
# var ground_height : int
# var game_running : bool
# var last_obs

# # Called when the node enters the scene tree for the first time.
# func _ready():
# 	screen_size = get_window().size
# 	ground_height = $Ground.get_node("Sprite2D").texture.get_height()
# 	$GameOver.get_node("Button").pressed.connect(new_game)
# 	new_game()

# func new_game():
# 	#reset variables
# 	score = 0
# 	show_score()
# 	game_running = false
# 	get_tree().paused = false
# 	difficulty = 0
	
# 	#delete all obstacles
# 	for obs in obstacles:
# 		obs.queue_free()
# 	obstacles.clear()
	
# 	#reset the nodes
# 	$Dino.position = DINO_START_POS
# 	$Dino.velocity = Vector2i(0, 0)
# 	$Camera2D.position = CAM_START_POS
# 	$Ground.position = Vector2i(0, 0)
	
# 	#reset hud and game over screen
# 	$HUD.get_node("StartLabel").show()
# 	$GameOver.hide()

# # Called every frame. 'delta' is the elapsed time since the previous frame.
# func _process(delta):
# 	if game_running:
# 		#speed up and adjust difficulty
# 		speed = START_SPEED + score / SPEED_MODIFIER
# 		if speed > MAX_SPEED:
# 			speed = MAX_SPEED
# 		adjust_difficulty()
		
# 		#generate obstacles
# 		generate_obs()
		
# 		#move dino and camera
# 		$Dino.position.x += speed
# 		$Camera2D.position.x += speed
		
# 		#update score
# 		score += speed
# 		show_score()
		
# 		#update ground position
# 		if $Camera2D.position.x - $Ground.position.x > screen_size.x * 1.5:
# 			$Ground.position.x += screen_size.x
			
# 		#remove obstacles that have gone off screen
# 		for obs in obstacles:
# 			if obs.position.x < ($Camera2D.position.x - screen_size.x):
# 				remove_obs(obs)
# 	else:
# 		if Input.is_action_pressed("ui_accept"):
# 			game_running = true
# 			$HUD.get_node("StartLabel").hide()

# func generate_obs():
# 	#generate ground obstacles
# 	if obstacles.is_empty() or last_obs.position.x < score + randi_range(300, 500):
# 		var obs_type = obstacle_types[randi() % obstacle_types.size()]
# 		var obs
# 		var max_obs = difficulty + 1
# 		for i in range(randi() % max_obs + 1):
# 			obs = obs_type.instantiate()
# 			var obs_height = obs.get_node("Sprite2D").texture.get_height()
# 			var obs_scale = obs.get_node("Sprite2D").scale
# 			var obs_x : int = screen_size.x + score + 100 + (i * 100)
# 			var obs_y : int = screen_size.y - ground_height - (obs_height * obs_scale.y / 2) + 5
# 			last_obs = obs
# 			add_obs(obs, obs_x, obs_y)
# 		#additionally random chance to spawn a bird
# 		if difficulty == MAX_DIFFICULTY:
# 			if (randi() % 2) == 0:
# 				#generate bird obstacles
# 				obs = bird_scene.instantiate()
# 				var obs_x : int = screen_size.x + score + 100
# 				var obs_y : int = bird_heights[randi() % bird_heights.size()]
# 				add_obs(obs, obs_x, obs_y)

# func add_obs(obs, x, y):
# 	obs.position = Vector2i(x, y)
# 	obs.body_entered.connect(hit_obs)
# 	add_child(obs)
# 	obstacles.append(obs)

# func remove_obs(obs):
# 	obs.queue_free()
# 	obstacles.erase(obs)
	
# func hit_obs(body):
# 	if body.name == "Dino":
# 		game_over()

# func show_score():
# 	$HUD.get_node("ScoreLabel").text = "SCORE: " + str(score / SCORE_MODIFIER)

# func check_high_score():
# 	if score > high_score:
# 		high_score = score
# 		$HUD.get_node("HighScoreLabel").text = "HIGH SCORE: " + str(high_score / SCORE_MODIFIER)

# func adjust_difficulty():
# 	difficulty = score / SPEED_MODIFIER
# 	if difficulty > MAX_DIFFICULTY:
# 		difficulty = MAX_DIFFICULTY

# func game_over():
# 	check_high_score()
# 	get_tree().paused = true
# 	game_running = false
# 	$GameOver.show()


               











main()

