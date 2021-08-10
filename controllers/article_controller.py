import json
from datetime import datetime

from constants import http_response
from dal.article_dao import ArticleDao
from messages.article import Article
from messages.article_content import ArticleContent


class ArticleController(object):
    def get(self, request):
        if not request.args or "id" not in request.args:
            return http_response.MISSING_PARAMETER
        id = request.args.get("id")
        try:
            article = ArticleDao.get(id)
            if article == None:
                article = {"status": "error"}

            def converter(o):
                return o.__str__()

            return (
                json.dumps(article, default=converter),
                200,
                http_response.DEFAULT_HEADERS,
            )
        except Exception as e:
            print(e)
        return json.dumps({"status": "ok"}), 200, http_response.DEFAULT_HEADERS

    def post(self, request):
        payload = request.get_json()
        needed_parameters = [
            "title",
            "subtitle",
            "body",
            "main_image",
            "author_name",
            "author_picture",
            "category",
            "tags",
            "time_to_read",
        ]
        if not all(elem in payload for elem in needed_parameters):
            return http_response.MISSING_PARAMETER

        title = payload["title"]
        subtitle = payload["subtitle"]
        body = payload["body"]
        main_image = payload["main_image"]
        author_name = payload["author_name"]
        author_picture = payload["author_picture"]
        category = payload["category"]
        tags = payload["tags"]
        time_to_read = payload["time_to_read"]

        article: Article = Article(
            ArticleContent(title, subtitle, body, main_image),
            author_name,
            author_picture,
            category,
            tags,
            time_to_read,
            [],
            datetime.now(),
            0,
        )
        ArticleDao.create(article)
        return json.dumps({"status": "ok"}), 200, http_response.DEFAULT_HEADERS


class ArticlesController(object):
    def get(self, request):
        try:
            articles = ArticleDao.get_all()
            if articles == None:
                articles = ""

            def converter(o):
                return o.__str__()

            return (
                json.dumps({"articles": articles}, default=converter),
                200,
                http_response.DEFAULT_HEADERS,
            )
        except Exception as e:
            print(e)
        return json.dumps({"articles": articles}), 200, http_response.DEFAULT_HEADERS
