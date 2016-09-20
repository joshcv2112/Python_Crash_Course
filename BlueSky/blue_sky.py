"""
Author: Joshua Vaughan
Created: September 2016
Exercise 12-1
Make a Pygame window with a blue background.
"""

import sys

import pygame

def run_game():
    # Initialize the game and create screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    # Set the background color to blue.
    bg_color = (0, 0, 225)

    # Start main game loop.
    while True:
        
        # Keyboard and mouse event handler.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        
        # Make currently drawn screen visible.
        pygame.display.flip()

run_game()