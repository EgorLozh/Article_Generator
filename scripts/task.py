from sqlalchemy import insert, select
import asyncio
from sqlalchemy.orm import Session

from llm_api.api import LLM_Qwen05B
from scripts.parsers.GetGoogleTrends import get_google_trends
from scripts.parsers.UniversalArticleParser import get_article
from src.articles.schemas import QueryCreate, ArticleCreate, Query as Query_s

from src.articles.models import Query, Article
from src.database import get_async_session


class Parse_task:
    def __init__(self, session):
        self.session = session

    async def start(self):
        google_trends = get_google_trends()
        queries = [QueryCreate.parse_obj(q) for q in google_trends]

        # Преобразование объектов Pydantic в словари
        queries_dicts = [query.dict() for query in queries]

        # Проверка на существование записей в базе данных
        existing_titles = set()
        existing_urls = set()

        async with self.session.begin():
            for query in queries_dicts:
                stmt = select(Query).where(
                    (Query.title == query['title']) | (Query.src_url == query['src_url'])
                )
                result = await self.session.execute(stmt)
                existing_query = result.scalars().first()
                if existing_query:
                    existing_titles.add(query['title'])
                    existing_urls.add(query['src_url'])

        # Отфильтровать только новые записи
        new_queries = [
            query for query in queries_dicts
            if query['title'] not in existing_titles and query['src_url'] not in existing_urls
        ]

        if new_queries:
            stmt = insert(Query).values(new_queries)
            async with self.session.begin():
                await self.session.execute(stmt)
                await self.session.commit()

class ArticleGenerator:
    def __init__(self, session):
        self.session = session
        self.llm_api = LLM_Qwen05B()

    async def generate_articles(self):
        # Получение всех запросов, для которых нет статей
        stmt = select(Query).outerjoin(Article, Query.id == Article.query_id).filter(Article.id == None)
        result = await self.session.execute(stmt)
        queries_without_articles = result.scalars().all()

        for query in queries_without_articles:
            try:
                article = get_article(query.src_url)
            except:
                continue
            prompt = (f"Напиши статью на тему: {query.title}, при написании основывайся на тексте оригинала вот он: "
                      f"{article} используй только основную информацию относящуюся к статье")
            system_context = ('Ты профессиональный журналист, который придерживается только фактов. Не придумывай новой'
                              ' информации, используй политкорректные высказывания')
            print(prompt)
            response = self.llm_api.get_request(prompt, system_context)
            print(response)
            article_data = ArticleCreate(query_id=query.id, text=response)
            stmt = insert(Article).values(article_data.dict())
            await self.session.execute(stmt)
            await self.session.commit()

async def main():
    async for session in get_async_session():
        parse_task = Parse_task(session)
        await parse_task.start()

        article_generator = ArticleGenerator(session)
        await article_generator.generate_articles()

if __name__ == "__main__":
    asyncio.run(main())
