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

        # Set up positions for animals
        self.pos1 = (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 3) # Top Left (Parent 1)
        self.pos2 = ((SCREEN_WIDTH / 4) * 3, SCREEN_HEIGHT / 3) # Top Right (Parent 2)
        self.pos3 = (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 3) * 2) # Bottom Center

        self.mumAnimal = None
        self.dadAnimal = None
        self.childAnimal = None

        # Set up the app loop
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        # Start the simulation
        self.start_sim()
        self.loop()

    def start_sim(self):
        self.mumAnimal = self.make_Animal(self.pos1)
        self.dadAnimal = self.make_Animal(self.pos2)
        logger.debug(f"Animal 1 {self.mumAnimal}")
        logger.debug(f"Animal 2 {self.dadAnimal}")

    def make_Animal(self, pos):
        # Initializes the simulation world.
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
        newAnimal = Animal((allSprites), pos, self.genome0, self.genome1)
        logger.info("Animal created.")
        newAnimal.select_genes()
        newAnimal.gene_math()
        newAnimal.express()
        return newAnimal
    
    def procreate(self, mum, dad):
        mumGenes = mum.select_chromosomes()
        logger.debug(f"Mum's Genes: {mumGenes}")
        dadGenes = dad.select_chromosomes()
        logger.debug(f"Dad's Genes: {dadGenes}")
        child = Animal((allSprites), self.pos3, mumGenes, dadGenes)
        child.select_genes()
        child.gene_math()
        child.express()
        return child

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.childAnimal is not None:
                    self.childAnimal.kill()
                self.childAnimal = self.procreate(self.mumAnimal, self.dadAnimal)
    
    def update(self):
        # Update all entities (sprites).
        allSprites.update(self.dt)
    
    def draw(self):
        # Draw everything to the screen
        self.screen.fill((0,0,0))
        allSprites.draw(self.screen)
        pygame.display.flip()