from fastapi import FastAPI
from try_fastapi.cel_app import fetch_response, get_status
import time

app = FastAPI()


@app.get('/')
def adding_task():
    response = fetch_response.delay()
    return response.id


@app.get('/status')
def task_status(task_id: str):
    status = get_status(task_id)
    return status
