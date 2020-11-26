from fastapi import APIRouter
import pika

from api.models import Task
from config import RABBITMQ_HOST, RABBITMQ_PORT

router = APIRouter()


@router.post("/add/")
async def endpoint(task: Task):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
    new_task = task.__dict__
    params = ""
    for param in new_task.get("params"):
        params += param + " " + new_task.get("params").get(param) + " "
    body = f'task - {new_task.get("task_id")} title - {new_task.get("title")} params - {params}'
    channel = connection.channel()
    channel.queue_declare(queue='task')
    channel.basic_publish(exchange='', routing_key='task',
                          body=body)
    connection.close()
    return f'send task #{new_task.get("task_id")}'
