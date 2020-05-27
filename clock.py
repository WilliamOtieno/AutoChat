from apscheduler.schedulers.blocking import BlockingScheduler
from chat import send_message

sched = BlockingScheduler()

sched.add_job(send_message, 'interval', seconds=5)
sched.start()
