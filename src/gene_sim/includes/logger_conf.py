import logging

# Set up basics
logging.basicConfig(filename="sim.log", filemode="a", format="%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S", level=logging.DEBUG) # Set up logging
logging.getLogger("werkzeug").disabled = False

# Create custom logger
logger = logging.getLogger("sim")

# Set log level
logger.setLevel(logging.DEBUG)

# Create handlers
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)

# Create formatters and add them to the handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)

# Add handlers to the logger
logger.addHandler(c_handler)