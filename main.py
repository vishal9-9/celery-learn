from celery import Celery


app = Celery('task', broker='amqp://localhost')


@app.task
def add(x, y):
    return x+y
