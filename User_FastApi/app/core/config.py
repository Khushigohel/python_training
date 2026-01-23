### database connections.....
import os

Database_URL= os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/user_taskDB"
)