from fastapi import FastAPI
from app.routes import users, groups

app = FastAPI(title="Predplat si API")

app.include_router(users.router, prefix="/users")
app.include_router(groups.router, prefix="/groups")