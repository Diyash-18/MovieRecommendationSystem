from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("URI")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")