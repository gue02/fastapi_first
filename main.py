from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/{username}")
def read_root(request: Request, username : str):
    # 2026.05.28 업데이트: Starlette 1.0 호환을 위해 request를 첫 번째 인자로 전달합니다.
    return templates.TemplateResponse(request, "index.html", {"username": username})