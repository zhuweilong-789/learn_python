from fastapi import APIRouter, Depends, Query

router = APIRouter(prefix="/news", tags=["news"])


class PaginationParams:
    """分页查询依赖，可被多个接口复用"""

    def __init__(self, page: int = Query(1, ge=1, description="页码，从 1 开始"),
                 size: int = Query(10, ge=1, le=100, description="每页数量，1-100")):
        self.page = page
        self.size = size

    @property
    def offset(self) -> int:
        """数据库查询用的偏移量"""
        return (self.page - 1) * self.size


@router.get("")
def list_news(pagination: PaginationParams = Depends(PaginationParams)):
    """获取新闻列表（支持分页）"""
    # 模拟数据
    all_news = [
        {"id": i, "title": f"示例新闻{i}"}
        for i in range(1, 26)  # 模拟 25 条数据
    ]

    start = pagination.offset
    end = start + pagination.size
    page_data = all_news[start:end]

    return {
        "news": page_data,
        "page": pagination.page,
        "size": pagination.size,
        "total": len(all_news),
    }
