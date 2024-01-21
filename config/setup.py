import os
from dotenv import load_dotenv

config_dir = os.path.dirname(__file__)
path = os.path.join(config_dir, '..', '.env')

load_dotenv(path)

NAME = os.getenv('NAME')
