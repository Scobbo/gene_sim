import pygame
import sys
from .sim_logic import Sim
from .includes.logger_conf import logger

if __name__ == '__main__':
    try:
        # Create an instance of the Sim class.
        sim = Sim()
        # Run the sim.
        sim.start_sim()
    except Exception as e:
        logger.exception("Simulation crashed with error: %s", e)
    finally:
        pygame.quit()
        sys.exit()