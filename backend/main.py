from fastapi import FastAPI
from loguru import logger

from backend.routes import router

app = FastAPI()

app.include_router(router)

logger.remove()

logger.add("./backend/logs/dev_backend.log",
          rotation="10 MB",
          retention="7 days",
          compression="zip",
          level="TRACE",
          enqueue=True,
          format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")