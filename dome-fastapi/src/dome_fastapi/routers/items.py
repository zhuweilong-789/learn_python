from fastapi import APIRouter

from ..models.item import Item

router = APIRouter(tags=["items"])


# 路径参数 item_id，查询参数 q
@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# item 是一个 Item 对象，作为请求体
@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item, "message": "这是返回的数据"}
