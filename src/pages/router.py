from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from articles.router import get_articles, get_detail_article

router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)

templates = Jinja2Templates(directory='templates')

@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})

@router.get("/list")
async def get_list_page(request: Request, articles=Depends(get_articles)):
    return templates.TemplateResponse('news_list.html', {'request': request, 'articles': articles})

@router.get("/detail/{article_id}")
async def get_detail_page(request: Request, article=Depends(get_detail_article)):
    return templates.TemplateResponse('detail.html', {'request': request, 'article': article})
