import random
from .logger_conf import logger

def rand_gene(genome):
        logger.debug(f"Randomising Genome")
        for i in genome:
            logger.debug(f"Itterating through Chromosomes")
            for j in range(5):
                j = (random.uniform(1,10), random.uniform(0,1))
                i.append(j)