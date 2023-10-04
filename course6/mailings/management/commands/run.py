from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from mailings.services import my_job

scheduler = BlockingScheduler()

scheduler.add_job(my_job, 'interval', seconds=30)

scheduler.start()
# from apscheduler.schedulers.background import BackgroundScheduler
#
# from mailings.services import my_job
#
# scheduler = BackgroundScheduler()
# job = None


def start_job():
    global job
    job = scheduler.add_job(my_job, 'interval', seconds=3600)
    try:
        scheduler.start()
    except:
        pass
