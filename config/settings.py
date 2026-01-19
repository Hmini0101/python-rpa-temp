import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"
