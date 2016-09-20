"""
Author: Joshua Vaughan
Created: September 2016
Exercise 12-2
Find an image of a game character, place it in the center of the screen
and match the background color of the image to the background of the screen.
"""

import sys

import pygame
from settings import Settings
from character import Character

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Special Mario Dudes!")

    # Make a character
    mario = Character(screen)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(game_settings.bg_color)
        mario.blitme()
        pygame.display.flip()

run_game()
