import os

from dotenv import load_dotenv

ROOT_FOLDER = os.getcwd()

load_dotenv(os.path.join(ROOT_FOLDER, '.env'))

host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 4
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    # UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    # ALLOWED_EXTENSIONS = ['pdf', 'csv']
    JWT_ACCESS_TOKEN_EXPIRES = False
