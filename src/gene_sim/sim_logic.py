import pygame
from .includes.config import TITLE, SCREEN_HEIGHT, SCREEN_WIDTH, FPS, allSprites
from .includes.calc import rand_gene
from .includes.entities import Animal
from .includes.logger_conf import logger

class Sim:
    def __init__(self):
        # Initialize Pygame
        logger.info("Setting up simulation")
        logger.info("Initialising pygame")
        pygame.init()

        # Set up the screen
        self.screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pygame.display.set_caption(TITLE)

        # Set up the app loop
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        # Start the simulation
        self.start_sim

    def start_sim(self):
        # Initializes the simulation world.
        # Step 0: Clean up old sprites if restarting (Not needed yet, but future proofing).
        allSprites.empty()
        # Make an animal
        self.chromosome0 = []
        self.chromosome1 = []
        self.chromosome2 = []
        self.chromosome3 = []
        self.chromosome4 = []
        self.chromosome5 = []
        self.genome = [self.chromosome0, self.chromosome1, self.chromosome2, self.chromosome3, self.chromosome4, self.chromosome5]
        genome0 = rand_gene(self.genome)
        genome1 = rand_gene(self.genome)
        Animal((allSprites), genome0, genome1)

    def loop(self):
        # Main app loop.
        while self.running:
            self.dt = self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Handle user input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
    
    def update(self):
        # Update all entities (sprites).
        allSprites.update(self.dt)
    
    def draw(self):
        # Draw everything to the screen
        self.screen.fill((0,0,0))
        allSprites.draw(self.screen)
        pygame.display.flip()