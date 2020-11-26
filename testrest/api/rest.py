from typing import Optional, Dict
from fastapi import APIRouter
import pika
from pydantic import BaseModel

router = APIRouter()


class Task(BaseModel):
    task_id: str
    title: str
    params: Optional[Dict] = None


@router.post("/add/")
async def endpoint(task: Task):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    new_task = task.__dict__
    params = ""
    for param in new_task.get("params"):
        params += param + " " + new_task.get("params").get(param)+" "
    body = f'task - {new_task.get("task_id")} title - {new_task.get("title")} params - {params}'
    channel = connection.channel()
    channel.queue_declare(queue='task')
    channel.basic_publish(exchange='', routing_key='task',
                          body=body)
    connection.close()
    return f'send task #{new_task.get("task_id")}'
