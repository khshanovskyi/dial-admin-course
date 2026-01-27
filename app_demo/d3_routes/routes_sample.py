import uvicorn
from fastapi import FastAPI, HTTPException, Header, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Tasks API", version="1.0.0")

# In-memory storage for tasks
tasks_db: dict[int, dict] = {}
task_id_counter = 1


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    """Create a new task."""
    global task_id_counter

    task_data = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }
    tasks_db[task_id_counter] = task_data
    task_id_counter += 1

    return task_data


@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    """Get a task by ID."""

    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    return tasks_db[task_id]

@app.get("/tasks", response_model=list[TaskResponse])
async def get_tasks():
    """Get all tasks."""

    return list(tasks_db.values())


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    """Delete a task by ID."""

    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    del tasks_db[task_id]
    return None


if __name__ == "__main__":
    uvicorn.run(app, port=5050, host="0.0.0.0")