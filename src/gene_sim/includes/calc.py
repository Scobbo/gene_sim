import random

def rand_gene(genome):
        for i in genome:
            for _ in range(5):
                i.append(random.uniform(1,10))