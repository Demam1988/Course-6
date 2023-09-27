from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(daemon=True)


def my_job():
    print("Hello, world!")


scheduler.add_job(my_job, 'interval', seconds=5)
scheduler.start()
