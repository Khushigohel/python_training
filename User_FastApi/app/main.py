from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import userRoutes,taskRoutes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Task API")

app.include_router(userRoutes.router)
app.include_router(taskRoutes.router)

