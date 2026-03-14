from fastapi import APIRouter

router = APIRouter(prefix="/users")

users_db = []

@router.post("/")
def create_user(user: dict):
    users_db.append(user)
    return user

@router.get("/")
def get_users():
    return users_db

@router.get("/{id}")
def get_user(id: int):
    return users_db[id]

@router.delete("/{id}")
def delete_user(id: int):
    users_db.pop(id)
    return {"message": "deleted"}