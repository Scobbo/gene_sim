import random
from .logger_conf import logger

def rand_gene(heplome):
        for i in heplome:
            for j in range(5):
                j = (random.uniform(1,10), random.uniform(0,1))
                i.append(j)