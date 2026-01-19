## NOTION DB 조회
from config.settings import BASE_URL, DATABASE_ID
from notion.client import post


def get_requested_tasks():
    url = f"{BASE_URL}/database/{DATABASE_ID}/query"
    body = {"filter": {"property": "Status", "select": {"equals": "요청"}}}

    res = post(url, body)
    return res.json()["results"]
