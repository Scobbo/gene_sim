import pygame
from .logger_conf import logger
from operator import itemgetter
from random import randint

class Animal(pygame.sprite.Sprite):
    def __init__(self, groups, pos, heplome0, heplome1):
        super().__init__(groups)
        # Full Genome
        self.heplome0 = heplome0
        self.heplome1 = heplome1
        self.activeGene = []

        # Attributes
        self.width = 10
        self.height = 10
        self.red = 128
        self.blue = 128
        self.green = 128

        # Visual
        self.image = pygame.Surface((20, 20))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_frect(center = pos)
    
    def select_genes(self):
        for i in range(len(self.heplome0)):
            for k, l in zip(self.heplome0[i], self.heplome1[i]):
                self.activeGene.append(max([k, l], key=itemgetter(1))[0])

    def select_chromosomes(self):
        logger.debug("Choosing chromosomes to pass on")
        chromosomeList = []
        for i in range(len(self.heplome0)):
            selector = randint(0,1)
            if selector == 0:
                chromosomeList.append(self.heplome0[i])
                logger.debug("Selected from heplome 0")
            else:
                chromosomeList.append(self.heplome1[i])
                logger.debug("Selected from heplome 1")
        return chromosomeList

    def gene_math(self):
        self.height = ((self.activeGene[0] + self.activeGene[3]) / 2) * 20
        logger.debug(f"Height: {self.height}")
        self.width = ((self.activeGene[1] + self.activeGene[4]) / 2) * 20
        logger.debug(f"Width: {self.width}")
        self.red = ((self.activeGene[2] + self.activeGene[1] + self.activeGene[5]) / 3) * 25
        self.green = ((self.activeGene[3] + self.activeGene[2] + self.activeGene[6]) / 3) * 25
        self.blue = ((self.activeGene[4] + self.activeGene[3] + self.activeGene[7]) / 3) * 25
        logger.debug(f"Colour: {self.red}, {self.green}, {self.blue}")

    def express(self):
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((int(self.red), int(self.green), int(self.blue)))