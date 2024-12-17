import uvicorn
from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router

app = FastAPI()

# Подключение маршрутов
app.include_router(task_router)
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)