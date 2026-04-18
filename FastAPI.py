

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()





task_db = []

class TaskCreate(BaseModel):
    title : str
    description : str
    owner : str

class TaskResponse(TaskCreate):
    id:int
    is_completed:bool


@app.post("/addtask",response_model=TaskResponse)
def add_task(TaskCreate):
    task_dict=task.dict()
    task_dict['id']=len(task_db)+1
    task_dict['is_completed'] = False
    task.db.append(task_dict)
    return task_dict

@app.get("/gettask")
def get_all_tasks():
    return task_db

@app.put("/completetask/{task_id}")
def complete_task(task_id:int):
    for task in task_db:
        if task['id'] == task_id:
            task['is_completed']=True
            return task
    raise HTTPException(status_code=404,detail="Task Not Found")