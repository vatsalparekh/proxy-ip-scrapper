from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from scraper.func import call_browser
from scraper.urlconfig import urls

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/5')),             ######################################To CHANGE TIME INTERVAL#######
    name="scraping data and pushing to database",
    ignore_result=True)
def main():
    url_index = 0
    while (url_index < len(urls)):
        call_browser(url_index)
        url_index += 1
