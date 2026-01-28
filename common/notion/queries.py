## NOTION DB 조회
from common.notion.client import NotionClient
from config.settings import NOTION_DATABASE_ID


class NotionQueryService:

    def __init__(self):
        self.client = NotionClient()
        self.database_id = NOTION_DATABASE_ID

    def fetch_all(self):
        """DB 전체 조회"""
        payload = {}
        return self.client.post(f"/databases/{self.database_id}/query", payload)

    def fetch_by_date(self, date_str: str):
        """특정 날짜 데이터 조회"""
        payload = {"filter": {"property": "날짜", "date": {"equals": date_str}}}
        return self.client.post(f"/databases/{self.database_id}/query", payload)
