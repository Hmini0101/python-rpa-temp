## NOTION API 클라이언트

import requests
from config.settings import NOTION_TOKEN, NOTION_VERSION

HEADERS = {
    "Authoriztion": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": NOTION_VERSION,
}


def post(url, body):
    return requests.post(url, headers=HEADERS, json=body)


def patch(url, body):
    return requests.patch(url, headers=HEADERS, json=body)
