import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MYSQL_HOST = os.getenv('DB_HOST', 'localhost')
    MYSQL_USER = os.getenv('DB_USER', 'root')
    MYSQL_PASSWORD = os.getenv('DB_PASSWORD', '')
    MYSQL_DB = os.getenv('DB_NAME', 'boss-spider')
    MYSQL_CURSORCLASS = 'DictCursor'
