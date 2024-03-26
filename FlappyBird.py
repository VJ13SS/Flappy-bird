'''HEY all this is a Simple Flapoy bird game demonstration build using pygame..Hope you enjoys it..
Note: all the coordinates selected here are with reference to my screen .. adjust for yours

link for inages zip file: https://dev-cms.us-east-1.linodeobjects.com/imgs_b286d95d6d.zip

link for sound zip file : https://www.sounds-resource.com/mobile/flappybird/sound/5309/
Notify me on future updates
 VJ 13 SS'''

import pygame
import time
import random

WIN_WIDTH = 2000
WIN_HEIGHT = 2500

 #Load images
 #made the images 2 times bigger than their actual size

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load('bird1.png')),pygame.transform.scale2x(pygame.image.load('bird2.png')),pygame.transform.scale2x(pygame.image.load('bird3.png'))]

 #Background image ans scaling it to fot the window
BG_IMG = pygame.transform.scale2x(pygame.image.load('bg.png'))
BG_SCALE = pygame.transform.scale(BG_IMG, (WIN_WIDTH, WIN_HEIGHT))

 #Bird and its scaling
BIRD = pygame.image.load('bird1.png')
BIRD_SCALE = pygame.transform.scale(BIRD,(170,120))

 #Base
BASE_IMG = pygame.image.load('base.png')
BASE_SCALE = pygame.transform.scale(BASE_IMG,(1500, 800))

 #pipe
PIPE_1 = pygame.image.load('pipe 1.png')
PIPE_2 = pygame.image.load('pipe 2.png')

 #Initialization
pygame.init()
SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#text font
LABEL_FONT = pygame.font.SysFont('comicsans',150)

 #display bird
def display_bird(x,y):
	SCREEN.blit(BIRD_SCALE,(x,y))

#obstacle collision
def obstacle_collision(bird_x, bird_y, pipe_2_x, pipe_2_height, pipe_gap,pipe_width):
    bird_width = BIRD_SCALE.get_width()
    bird_height = BIRD_SCALE.get_height()  # Get the height of the bird
    
    #Checks if the bird is in the gap between the pipea and if it collides with either the top or the bottom pipe
    if (bird_x + bird_width >= pipe_2_x and bird_x <= pipe_2_x + pipe_width) and (bird_y <= pipe_2_height or bird_y + bird_height >= pipe_2_height + pipe_gap):
        return True
    return False

#play sound
def woosh_sound():
	sound = pygame.mixer.Sound('flappy_whoosh-43099.mp3')
	sound.play()

#point sound
def point_sound():
	sound = pygame.mixer.Sound('sfx_point.wav')
	sound.play()
	
#hit sound
def hit_sound():
	sound = pygame.mixer.Sound('sfx_hit.wav')
	sound.play()	

#display score
def draw_score(score,SCREEN):
	text_label = LABEL_FONT.render(f'Score: {score} ',1,'red')	
	SCREEN.blit(text_label, (500,550))

def main():
	#Initialized bird's position
	bird_x = 50#kept constant
	bird_y = 500
	bird_y_change = 0 #Initailly no change
	bird_gravity = 2.5#gravity 
	bird_base_pos = 1950
	
	#initialized pipe parameters
	pipe_gap= 400
	pipe_width = 200
	pipe_1_height = 775#initially
	pipe_x = 850
	pipe_x_change = -25
	
	#initialized score
	score = 0
	display_bird(bird_x,bird_y)
	running = True
	while running:
		
		SCREEN.fill((0,0,0))
		#Fitting the screen with image
		SCREEN.blit(BG_SCALE, (0,0))
		#Displays the base
		SCREEN.blit(BASE_SCALE, (0,bird_base_pos))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			
			#game starts by ckicking on the window or by pressing the space key
			elif event.type == pygame.MOUSEBUTTONDOWN or event.type  == pygame.KEYDOWN and (event.key == pygame.K_SPACE):
				
				bird_y_change = -30#bird moves up
				#plays sound
				woosh_sound()
		if bird_y_change < 0:
			bird_gravity = 1.5
		else:
			bird_gravity = 2.5
		bird_y_change += bird_gravity
		#Gravity at each time the bird rises up
	
		#Updated the birds position
		bird_y += bird_y_change
		
		
		#displays the bird
		display_bird(bird_x,bird_y)

		if bird_y <0 :
			bird_y = 0
		elif bird_y > bird_base_pos:
			bird_y = bird_base_pos
			
			#Declaring height of pipe 2		
		pipe_2_height = bird_base_pos - pipe_1_height- pipe_gap
			
		#Scaling pipes		
		PIPE_1_SCALE = pygame.transform.scale(PIPE_1,(pipe_width,pipe_1_height))
		PIPE_2_SCALE = pygame.transform.scale(PIPE_2,(pipe_width,pipe_2_height))
		
		#Displays obstacles(pipe)
		new_y = bird_base_pos - pipe_1_height
		SCREEN.blit(PIPE_1_SCALE, (pipe_x,new_y))
		SCREEN.blit(PIPE_2_SCALE, (pipe_x,0))
		
		#movement of pipes
		pipe_x += pipe_x_change
		if pipe_x < -100:
			pipe_x = 900
			#new height will generate only when the above condition is satisfied
			pipe_1_height = random.randint(0, 900)
		
		#checks collision
		if obstacle_collision(bird_x, bird_y, pipe_x, pipe_2_height, pipe_gap,pipe_width):
			
			hit_sound()
			#Re-initialization for end screen
			bird_y = bird_base_pos
			
			bird_y = 500
			bird_y_change = 0
			bird_gravity = 0
			pipe_x_change = 0
			pipe_x = 900
			mouse_x,mouse_y = pygame.mouse.get_pos()
			
			#Restarts the game			
			main()
					
		if  (bird_x + 170)//2 >= (pipe_x + pipe_width):
			#170 bird width
			#update score
			score += 1
			
			point_sound()
		draw_score(score,SCREEN)
	
		#update display
		pygame.display.update()
if __name__ =='__main__':
	main()
	

	
