from .items import router as items_router
from .users import router as users_router
from .books import router as books_router
from .pages import router as pages_router
from .news import router as news_router

__all__ = ["items_router", "users_router", "books_router", "pages_router", "news_router"]
