from celery import shared_task
from celery import Celery
from time import sleep

celery = Celery('tasks', broker='redis://localhost:6379/0')

@shared_task(bind=True)
def go_to_sleep(self, duration):
    sleep(duration)
    return 'Done'
