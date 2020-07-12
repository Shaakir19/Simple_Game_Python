# Task Number : 1
# File Name : my_first_game.py
# Written by : Shaakir Caroto
# Date Written : 13/02/2020
# The funtion of the program : This program is a simple game

# Imports a game library that lets you use specific functions in your program.
import pygame
# Import to generate random numbers. 
import random

# Initialize the pygame modules to get everything started.
pygame.init()

# The screen that will be created needs a width and a height.
display_width = 1100
display_height = 600
# This creates the screen and gives it the width and height specified as a 2 item sequence.
game_display = pygame.display.set_mode((display_width, display_height))

# This gives the game display a caption 
pygame.display.set_caption("My First Game")

# This creates the player and gives it the image found in this folder  
pac_player = pygame.image.load("player.jpg")

# Get the width and height of the images in order to do boundary detection
player_width = pac_player.get_width()
player_height = pac_player.get_height()

# Store the positions of the player as variables 
pac_x_pos = 100
pac_y_pos = 50

# This creates the enemies and gives it the image found in this folder  
mon_enemy_1 = pygame.image.load("monster.jpg")
mon_enemy_2 = pygame.image.load("monster.jpg")
mon_enemy_3 = pygame.image.load("monster.jpg")

# Get the width and height of the images in order to do boundary detection
mon_width_1 = mon_enemy_1.get_width() 
mon_height_1 = mon_enemy_1.get_height() 

mon_width_2 = mon_enemy_2.get_width() 
mon_height_2 = mon_enemy_2.get_height() 

mon_width_3 = mon_enemy_3.get_width() 
mon_height_3 = mon_enemy_3.get_height() 

# Make the enemy start off screen and at a random y position.
mon_1_x = display_width 
mon_1_y = random.randint(0, (display_height - mon_height_1))

mon_2_x = display_width
mon_2_y = random.randint(0, (display_height - mon_height_2))

mon_3_x = display_width 
mon_3_y = random.randint(0, (display_height - mon_height_3))

# This creates the player and gives it the image found in this folder 
prize_win = pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection
prize_width = prize_win.get_width()
prize_height = prize_win.get_height()

# Make the enemy start off screen and at a random y position.
prize_x_pos = display_width 
prize_y_pos = random.randint(0 , display_height - prize_height)

# This checks if the up or down key is pressed.
up_key = False
down_key = False
left_key = False
right_key = False

# This is the game loop.
while 1:

    # This is a looping structure that will loop the indented code until you tell it to stop
    # Clears the screen. 
    game_display.fill(0)
    # This draws the images to the screen at the postion specfied.
    game_display.blit(pac_player, (pac_x_pos, pac_y_pos))
    game_display.blit(mon_enemy_1, (mon_1_x, mon_1_y))
    game_display.blit(mon_enemy_2, (mon_2_x, mon_2_y))
    game_display.blit(mon_enemy_3, (mon_3_x, mon_3_y))
    game_display.blit(prize_win, (prize_x_pos, prize_y_pos))

    # This updates the screen.
    pygame.display.flip()

    # This loops through events in the game.
    for event in pygame.event.get():
         
        # This event checks if the user quits the program, then if so it exits the program. 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
 
        # This event checks if the user press a key down.
        if event.type == pygame.KEYDOWN:
            # Test if the key pressed is the one we want
            if event.key == pygame.K_UP:
                up_key = True
            if event.key == pygame.K_DOWN:
                down_key = True
        
        # This event checks if the user press a key down.
        if event.type == pygame.KEYDOWN:
            # Test if the key pressed is the one we want
            if event.key == pygame.K_RIGHT:
                right_key = True
            if event.key == pygame.K_LEFT:
                left_key = True

        # This event checks if the key is up
        if event.type == pygame.KEYUP:
            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                up_key = False
            if event.key == pygame.K_DOWN:
                down_key = False

        # This event checks if the key is up
        if event.type == pygame.KEYUP:
            # Test if the key released is the one we want.
            if event.key == pygame.K_RIGHT:
                right_key = False
            if event.key == pygame.K_LEFT:
                left_key = False
                
    # If the up_key varible is true 
    if up_key == True:
       # This makes sure that the user does not move the player above the window.
      if pac_y_pos > 0:
         pac_y_pos -= 1

    # If the down_key varible is true 
    if down_key == True:
        # This makes sure that the user does not move the player below the window.
        if pac_y_pos < display_height - player_height:
         pac_y_pos += 1

    # If the left_key varible is true 
    if left_key == True:
        # This makes sure that the user does not move the player out of the window.
        if pac_x_pos > 0:
         pac_x_pos -= 1

    # If the right_key varible is true 
    if right_key == True:
        # This makes sure that the user does not move the player out of the window.
        if pac_x_pos < display_width - player_width:
         pac_x_pos += 1 

    # Setting the bounder box for the player
    pac_box = pygame.Rect(pac_player.get_rect())
    # Setting the top as the y position of the box
    pac_box.top = pac_y_pos
    # Setting the left as the x position of the box
    pac_box.left = pac_x_pos

    # Setting the bounder box for the enemy
    mon_box_1 = pygame.Rect(mon_enemy_1.get_rect())
    # Setting the top as the y position of the box
    mon_box_1.top = mon_1_y
    # Setting the left as the x position of the box
    mon_box_1.left = mon_1_x

    # Setting the bounder box for the enemy
    mon_box_2 = pygame.Rect(mon_enemy_2.get_rect())
    # Setting the top as the y position of the box
    mon_box_2.top = mon_2_y
    # Setting the left as the x position of the box
    mon_box_2.left = mon_2_x
    
    # Setting the bounder box for the enemy
    mon_box_3 = pygame.Rect(mon_enemy_3.get_rect())
    # Setting the top as the y position of the box
    mon_box_3.top = mon_3_y
    # Setting the left as the x position of the box
    mon_box_3.left = mon_3_x

    # Setting the bounder box for the prize
    prize_box = pygame.Rect(prize_win.get_rect())
    # Setting the top as the y position of the box 
    prize_box.top = prize_y_pos
    # Setting the left as the x position of the box
    prize_box.left = prize_x_pos

    # This statement check if the box tounches an enemy
    if pac_box.colliderect(mon_box_1):
     # Displays you lose
     print("You lose!")
     # Closes the game
     pygame.quit()
     exit(0)
    
    # This statement check if the box tounches an enemy
    if pac_box.colliderect(mon_box_2):
     # Displays you lose
     print("You lose!")
     # Closes the game
     pygame.quit()
     exit(0)

    # This statement check if the box tounches an enemy
    if pac_box.colliderect(mon_box_3):
      # Displays you lose
     print("You lose!")
     # Closes the game
     pygame.quit()
     exit(0) 

    # This statement check if the box tounches the prize
    if pac_box.colliderect(prize_box):
      # Displays you win
     print("You win!")
      # Exits the game
     pygame.quit()
     exit(0)

    # Makes the object move toward the player 
    # Sets the speed of the objects
    mon_1_x -= 0.15
    mon_2_x -= 0.30
    mon_3_x -= 0.20
    prize_x_pos -= 0.1
