from fastapi import FastAPI, Request
from fastapi.responses import Response

from .routers import books_router, items_router, pages_router, users_router, news_router

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """记录每个请求的中间件"""
    print("中间件执行了")
    print("请求参数", request)
    response: Response = await call_next(request)
    return response


@app.get("/")
def read_root():
    return {"Hello": "World"}


# 常见的列表分页查询例子
@app.get("/list")
async def read_list(page: int = 1, size: int = 10):
    return {"list": f"查询列表{page}，每页{size}"}


# 挂载各业务路由
app.include_router(items_router)
app.include_router(users_router)
app.include_router(books_router)
app.include_router(news_router)
app.include_router(pages_router)
