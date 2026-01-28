import os
from dotenv import load_dotenv

load_dotenv()

# Notion
NOTION_BASE_URL = os.getenv("NOTION_BASE_URL", "https://api.notion.com/v1")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_VERSION = os.getenv("NOTION_VERSION", "2022-06-28")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
# Gmail
GMAIL_SENDER = os.getenv("GMAIL_SENDER")

# Runtime
ENV = os.getenv("ENV", "local")
