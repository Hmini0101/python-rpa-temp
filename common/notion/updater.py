## NOTION PAGE 상태업데이트
from config.settings import BASE_URL
from notion.client import patch


def update_status(page_id, status, result=None):
    body = {"properties": {"Status": {"select": {"name": status}}}}

    if result:
        body["properties"]["Result"] = {"rich_text": [{"text": {"content": result}}]}

    url = f"{BASE_URL}/pages/{page_id}"
    patch(url, body)
