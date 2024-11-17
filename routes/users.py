from fastapi import APIRouter

router = APIRouter()

@router.get("/users/")
async def fetch_users():
    return [{"username": "Rick"}, {"username": "Morty"}]