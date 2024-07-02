import os
from dotenv import load_dotenv
from alembic import context

load_dotenv()
db_url = os.getenv("DB_URL")

