import pygame
from .includes.config import TITLE, SCREEN_HEIGHT, SCREEN_WIDTH, FPS, allSprites
from .includes.calc import rand_gene
from .includes.entities import Animal
from .includes.logger_conf import logger

class Sim:
    def __init__(self):
        # Initialize Pygame
        logger.info(TITLE)
        logger.info("Setting up simulation")
        logger.info("Initialising pygame")
        pygame.init()

        # Set up the screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        logger.info(f"Screen size set to {SCREEN_WIDTH} x {SCREEN_HEIGHT}")

        # Set up the app loop
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        # Start the simulation
        self.start_sim()
        self.loop()

    def start_sim(self):
        # Initializes the simulation world.
        # Step 0: Clean up old sprites if restarting (Not needed yet, but future proofing).
        allSprites.empty()
        # Make an animal
        self.chromosomeA0 = []
        self.chromosomeA1 = []
        self.chromosomeB0 = []
        self.chromosomeB1 = []
        self.chromosomeC0 = []
        self.chromosomeC1 = []
        self.chromosomeD0 = []
        self.chromosomeD1 = []
        self.chromosomeF0 = []
        self.chromosomeF1 = []
        self.chromosomeG0 = []
        self.chromosomeG1 = []
        self.genome0 = [self.chromosomeA0, self.chromosomeB0, self.chromosomeC0, self.chromosomeD0, self.chromosomeF0, self.chromosomeG0]
        self.genome1 = [self.chromosomeA1, self.chromosomeB1, self.chromosomeC1, self.chromosomeD1, self.chromosomeF1, self.chromosomeG1]
        rand_gene(self.genome0)
        rand_gene(self.genome1)
        newAnimal = Animal((allSprites), self.genome0, self.genome1)
        logger.info("Animal created.")
        newAnimal.select_genes()
        newAnimal.gene_math()
        newAnimal.express()

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