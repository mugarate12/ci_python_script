import os
from dotenv import load_dotenv

config_dir = os.path.dirname(__file__)
path = os.path.join(config_dir, '..', '.env')

load_dotenv(path)

NAME = os.getenv('NAME')

DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
