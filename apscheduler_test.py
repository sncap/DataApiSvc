"""
Demonstrates how to use the blocking scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    print('Start time is: %s' % datetime.now())
    scheduler = BlockingScheduler()
    #"port": 26257, "user": "maxroach", "db": "yebb"}
    #url = 'cockroachdb://{}:{}@{}:{}/{}'.format("maxroach", '', '127.0.0.1', 26257, "yebb")
    #scheduler.add_jobstore('sqlalchemy', url=url)
    #sched.add_job(job, 'cron', second='*/5', id="test_1")
    scheduler.add_job(tick, 'cron', minute ='25,26,27' , id="test_1")
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass