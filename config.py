import os
from dotenv import load_dotenv
from sqlalchemy import URL


load_dotenv()

DB_HOST = str(os.environ.get("DB_HOST"))
DB_PORT = str(os.environ.get("DB_PORT"))
DB_NAME = str(os.environ.get("DB_NAME"))
DB_USER = str(os.environ.get("DB_USER"))
DB_PASS = str(os.environ.get("DB_PASS"))

POSTGRES_URI = os.environ.get("POSTGRES_URI")

SQLITE_ALCHIMY_URL = "sqlite+aiosqlite:///sqlite.db"
POSTGRES_ALCHIMY_URL = f"postgresql+asyncpg://{POSTGRES_URI}"


TICKET_CONFIG = {
    'price': 0.8,
    'description': '1e62222fb5e0fead',
    'timezone': 'Europe/Moscow',
    'timedelta': 30
}
