from fastapi import APIRouter

from ..models.user import User

router = APIRouter(tags=["users"])


# 通过提交表单例子来说明常见的 post 请求
@router.post("/submit")
def submit_form(user: User):
    return {"user": user, "message": "用户提交成功"}
