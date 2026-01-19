from notion.queries import get_requested_tasks
from notion.updater import update_status
from tasks.sample_task import SampleTask


def run():
    tasks = get_requested_tasks()

    for task in tasks:
        page_id = task["id"]
        update_status(page_id, "처리중")

        try:
            result = SampleTask().run()
            update_status(page_id, "완료", result)
        except Exception as e:
            update_status(page_id, "실패", str(e))
