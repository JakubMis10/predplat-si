from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_group():
    return {"message": "Group created"}

@router.get("/")
async def list_groups():
    return {"groups": []}