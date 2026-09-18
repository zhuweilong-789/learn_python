from datetime import date
from enum import Enum

from pydantic import BaseModel, Field, field_validator


class BookCategory(str, Enum):
    """图书分类枚举"""
    FICTION = "fiction"          # 小说
    SCIENCE = "science"          # 科技
    HISTORY = "history"          # 历史
    EDUCATION = "education"      # 教育
    OTHER = "other"              # 其他


class Book(BaseModel):
    """新增图书请求模型"""
    title: str = Field(..., min_length=1, max_length=100, description="书名（1-100 字）")
    author: str = Field(..., min_length=1, max_length=50, description="作者（1-50 字）")
    price: float = Field(..., gt=0, description="价格，必须大于 0")
    isbn: str = Field(..., pattern=r"^\d{10}(\d{3})?$", description="ISBN，10 或 13 位数字")
    publication_year: int = Field(..., ge=0, le=date.today().year, description="出版年份，不超过当前年份")
    stock: int = Field(0, ge=0, description="库存数量，不能为负")
    category: BookCategory = BookCategory.OTHER
    description: str | None = Field(None, max_length=500, description="图书简介，最多 500 字")

    @field_validator("title", "author")
    @classmethod
    def strip_whitespace(cls, v: str) -> str:
        """去除首尾空白后再校验，防止只传空格"""
        stripped = v.strip()
        if not stripped:
            raise ValueError("不能为空字符串")
        return stripped
