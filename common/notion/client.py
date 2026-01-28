## NOTION API 클라이언트

import requests
from config.settings import NOTION_BASE_URL, NOTION_API_KEY, NOTION_VERSION


class NotionClient:
    def __init__(self):
        self.base_url = NOTION_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {NOTION_API_KEY}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }

    def post(self, endpoint: str, payload: dict):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def patch(self, endpoint: str, payload: dict):
        url = f"{self.base_url}{endpoint}"
        response = requests.patch(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()
