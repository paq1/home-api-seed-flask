import os
from configparser import SafeConfigParser

from dotenv import load_dotenv


class Configuration:
    def __init__(self):
        load_dotenv()
        self.config = SafeConfigParser(os.environ)
        self.config.read('config.ini')
