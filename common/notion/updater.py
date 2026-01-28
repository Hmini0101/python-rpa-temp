## NOTION PAGE 상태업데이트
from common.notion.client import NotionClient
from common.notion.queries import NotionQueries
from common.notion.mapper import NotionMapper
from config.settings import NOTION_DATABASE_ID


class NotionUpdater:
    """Notion Database 에 데이터를 실제로 Insert/Update 하는 역할"""

    def __init__(self):
        self.client = NotionClient()
        self.queries = NotionQueries()
        self.mapper = NotionMapper()

    def insert_market_summary(
        self,
        date: str,  # 날짜
        sector: str,  # 주식섹터
        top_stocks: list,  # 순위
        total_volume: int,  # 거래대금
    ):

        properties = self.mapper.build_market_summary_properties(
            date=date, sector=sector, top_stocks=top_stocks, total_volume=total_volume
        )
        payload = {
            "parent": {"database_id": NOTION_DATABASE_ID},
            "properties": properties,
        }

        return self.client.create_page(payload)
