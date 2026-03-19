import pygame
from stickman import Stickman
from game import Game

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('8-bit Stickman Fighting Game')

def main():
    game = Game(WIN)
    game.run()

if __name__ == '__main__':
    main()