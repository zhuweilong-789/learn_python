from fastapi import APIRouter, HTTPException, status

from ..models.book import Book

router = APIRouter(prefix="/books", tags=["books"])

# 内存存储，仅作演示（真实项目应使用数据库）
BOOKS_DB: list[Book] = []


# 新增图书接口：演示 Pydantic 的字段校验与 HTTP 状态码
@router.post("", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    """新增一本图书"""
    # 简单去重：同一 ISBN 不允许重复新增
    if any(b.isbn == book.isbn for b in BOOKS_DB):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"ISBN 为 {book.isbn} 的图书已存在",
        )
    BOOKS_DB.append(book)
    return {"book": book, "message": "图书新增成功"}
