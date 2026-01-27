import uvicorn
from fastapi import FastAPI, HTTPException, Header, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Tasks API", version="1.0.0")

# API Key for authentication
API_KEY = "123456789"

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


def verify_api_key(api_key: Optional[str] = Header(None)) -> None:
    """Verify the API key from request header."""
    print("api-key")
    if api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-Api-Key header is missing"
        )
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate, api_key: Optional[str] = Header(None)):
    """Create a new task."""
    global task_id_counter

    verify_api_key(api_key)

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
async def get_task(task_id: int, api_key: Optional[str] = Header(None)):
    """Get a task by ID."""
    print("get")
    verify_api_key(api_key)

    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    return tasks_db[task_id]

@app.get("/tasks", response_model=list[TaskResponse])
async def get_tasks(api_key: Optional[str] = Header(None)):
    """Get all tasks."""
    verify_api_key(api_key)

    return list(tasks_db.values())


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, api_key: Optional[str] = Header(None)):
    """Delete a task by ID."""
    verify_api_key(api_key)

    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    del tasks_db[task_id]
    return None


if __name__ == "__main__":
    uvicorn.run(app, port=5051, host="0.0.0.0")