from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get('/')
def home(request: Request):
    context = {
        'request': request
    }
    return templates.TemplateResponse('general_pages/login.html', context)
