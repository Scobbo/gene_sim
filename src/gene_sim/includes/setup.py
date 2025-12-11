import pygame
from .logger_conf import logger
from .config import SCREEN_HEIGHT, SCREEN_WIDTH

def init_game():
    # Initialize Pygame
    logger.info("Setting up simulation...")
    logger.info("Initialising pygame")
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sim")

    # icon = pygame.image.load('assets/icon.png')
    # pygame.display.set_icon(icon)

    # Set up logic
    running = True
    clock = pygame.time.Clock()

    return screen, running, clock