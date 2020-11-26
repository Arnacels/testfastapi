from typing import Optional, Dict
from pydantic import BaseModel


class Task(BaseModel):
    task_id: str
    title: str
    params: Optional[Dict] = None