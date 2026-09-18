from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["pages"])


@router.get("/hello", response_class=HTMLResponse)
def hello_page(name: str = "World"):
    """返回一个简单的 HTML 页面，name 为查询参数"""
    html = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>欢迎</title>
        <style>
            body {{
                font-family: -apple-system, "PingFang SC", sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: #fff;
            }}
            .card {{
                text-align: center;
                padding: 2rem 3rem;
                background: rgba(255, 255, 255, 0.15);
                border-radius: 16px;
                backdrop-filter: blur(10px);
            }}
            h1 {{ margin: 0 0 0.5rem; font-size: 2.5rem; }}
            p  {{ margin: 0; opacity: 0.9; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>你好，{name}！</h1>
            <p>这是 FastAPI 返回的 HTML 页面</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)
