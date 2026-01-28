class NotionMapper:

    @staticmethod
    def build_market_summary_properties(date, sector, top_stocks, total_volume):
        return {
            "날짜": {"date": {"start": date}},
            "섹터": {"select": {"name": sector}},
            "상위종목": {"multi_select": [{"name": s} for s in top_stocks]},
            "거래대금": {"number": total_volume},
        }
