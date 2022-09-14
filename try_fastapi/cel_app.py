import time
from celery import Celery
import requests


celery_app = Celery('worker', backend='rpc://', broker='amqp://localhost')


@celery_app.task()
def fetch_response():
    response = requests.get('http://127.0.0.1:8002/user')
    return response.status_code


def get_status(task_id):
    status = celery_app.AsyncResult(task_id)
    return f'status: {status.status} and output: {status.result}'
