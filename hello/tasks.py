import time
from celery import Celery
from hello import settings
from hello import core

app = Celery(
    broker=settings.BROKER_URL,
    backend=settings.RESULT_BACKEND_URL)

app.conf.task_default_queue = settings.DEFAULT_QUEUE
app.conf.worker_send_task_events = True
app.conf.task_track_started = True


@app.task(bind=True, name='hello.ping')
def ping(self, seconds):
    print('---> hello.ping')
    time.sleep(seconds)
    print('<--- pong')
    return 'pong'


@app.task(bind=True, name='hello.get_items')
def get_items(self, size):
    items = [item for item in range(1, size + 1)]
    return items


@app.task(bind=True, name='hello.is_odd')
def is_odd(self, number):
    if type(number) == list:
        return [item % 2 != 0 for item in number]
    return number % 2 != 0


@app.task(bind=True, name='hello.send_notification')
def send_notification(self):
    return 'Success'


@app.task(bind=True, name='hello.unstable_task',
          autoretry_for=(Exception,),
          default_retry_delay=2,
          retry_kwargs={'max_retries': 3})
def unstable_task(self, inputs):
    core.run_unstable_task('a')
