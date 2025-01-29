import logging

def setup_logging():
    logging.basicConfig(logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')