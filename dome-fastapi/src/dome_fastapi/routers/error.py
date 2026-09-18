from fastapi import APIRouter
from fastapi.exceptions import HTTPException

router = APIRouter(tags=["error"])

@router.get("/error")
def read_error():
    raise HTTPException(status_code=404, detail="Not Found")