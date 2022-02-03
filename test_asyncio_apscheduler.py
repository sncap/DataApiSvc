# 사용방법

# 스케줄 종류에는 여러가지가 있는데 대표적으로 BlockingScheduler, BackgroundScheduler 입니다
# BlockingScheduler 는 단일수행에, BackgroundScheduler은 다수 수행에 사용됩니다.
# 여기서는 BackgroundScheduler 를 사용하겠습니다.
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import asyncio
from datetime import datetime
import os

def get_order_detail(s, orderNum, ems_yn, site = "KR"):
    print('Hello, get_order_detail!')
    order_detail_list = []
    order_detail_list.append(["t1", "t2"])
    return order_detail_list

async def run_routines(coroutine, session, order_list):
    #s = time.time()
    ret_lists = []
    row_cnt = 0
    functions = {coroutine(session, list[2], list[4]) for list in order_list}
    for func in asyncio.as_completed(functions):
        data = await func
        ret_lists.append(data)
        row_cnt += 1
        print('.', end='')
        if row_cnt % 50 == 0:
            print("(cnt = %s)" % row_cnt)

    print("(cnt = %s)" % row_cnt)
    print("")
    #print(data)

    return ret_lists
    #print(f'Resonse from: {url}, {len(body)}Bytes - {f}sec')
    #print(f'{time.time() - s:0.3f}sec')

async def get_scraping_data(session, orderNum, ems_yn):
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, get_order_detail, session, orderNum, ems_yn)
    data = res[0]
    #data = res.read().decode()
    return data

def sync_order_result_by_order_num_from_order_plan():
    loop = asyncio.new_event_loop()
    # get_order_detail = get_scraping_data
    order_list = [["dep_date", "dep_time", "order_num", "order_date", "ems_yn", "status"]]
    session = ""

    order_detail_list = loop.run_until_complete(run_routines(get_scraping_data, session, order_list))
    loop.close()


if __name__ == '__main__':
    print('Start time is: %s' % datetime.now())
    scheduler = BlockingScheduler()
    #"port": 26257, "user": "maxroach", "db": "yebb"}
    #url = 'cockroachdb://{}:{}@{}:{}/{}'.format("maxroach", '', '127.0.0.1', 26257, "yebb")
    #scheduler.add_jobstore('sqlalchemy', url=url)

    scheduler.add_job(sync_order_result_by_order_num_from_order_plan, 'cron', second='*/3', id="test_1")
    #scheduler.add_job(get_order_result, 'cron', minute ='43, 44, 45, 46, 25,26,27' , id="test_1")
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


'''
# BackgroundScheduler 를 사용하면 stat를 먼저 하고 add_job 을 이용해 수행할 것을 등록해줍니다.
sched = BackgroundScheduler()
#sched = AsyncIOScheduler()
sched.start()


sched.add_job(job3, 'interval', seconds=2, id="jobid3")


# interval - 매 3조마다 실행
sched.add_job(show_hello, 'interval', seconds=5, id="test_3")
sched.add_job(job, 'interval', seconds=3, id="test_2")

# cron 사용 - 매 5초마다 job 실행
# 	: id 는 고유 수행번호로 겹치면 수행되지 않습니다.
# 	만약 겹치면 다음의 에러 발생 => 'Job identifier (test_1) conflicts with an existing job'
sched.add_job(job, 'cron', second='*/5', id="test_1")

# cron 으로 하는 경우는 다음과 같이 파라미터를 상황에 따라 여러개 넣어도 됩니다.
# 	매시간 59분 10초에 실행한다는 의미.
sched.add_job(job_2, 'cron', minute="59", second='10', id="test_10")

count = 0
while True:
    print("Running main process...............")
    time.sleep(1)

'''
