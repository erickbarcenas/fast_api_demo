from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get('/login')
def home(request: Request):
    context = {
        'request': request
    }
    return templates.TemplateResponse('general_pages/login.html', context)
