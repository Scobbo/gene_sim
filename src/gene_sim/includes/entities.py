import pygame
import random
from .config import SCREEN_HEIGHT, SCREEN_WIDTH

class Animal(pygame.sprite.Sprite):
    def __init__(self, groups, genome0, genome1):
        super().__init__(groups)
        # Parent Genes
        self.genome0 = genome0
        self.genome1 = genome1

        # Activated Genes
        self.chromosome0 = []
        self.chromosome1 = []
        self.chromosome2 = []
        self.chromosome3 = []
        self.chromosome4 = []
        self.chromosome5 = []
        self.genome = [self.chromosome0, self.chromosome1, self.chromosome2, self.chromosome3, self.chromosome4, self.chromosome5]

        # Attributes
        self.width = 10
        self.height = 10
        self.red = 128
        self.blue = 128
        self.green = 128

        # Visual
        self.image = pygame.Surface((20, 20))
        self.image.fill(128, 128, 128)
        self.rect = self.image.get_frect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    
    def select_genes(self):
        for i in self.genome:
            for j in i:
                

    def gene_math(self):
        self.height = ((self.chromosome0[0] + self.chromosome3[3]) / 2) * 20
        self.width = ((self.chromosome0[1] + self.chromosome3[4]) / 2) * 20
        self.red = ((self.chromosome0[2] + self.chromosome4[1] + self.chromosome3[5]) / 3) * 25
        self.green = ((self.chromosome0[3] + self.chromosome4[2] + self.chromosome3[6]) / 3) * 25
        self.blue = ((self.chromosome0[4] + self.chromosome4[3] + self.chromosome3[7]) / 3) * 25

    def express(self):
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.red, self.green, self.blue)

    def rand_gene(self):
        for i in self.genome:
            for _ in range(10):
                i.append(random.uniform(0,10))