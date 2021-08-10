from typing import List, Union

from google.cloud import firestore
from messages.article import Article

client = firestore.Client()


class ArticleDao:
    def create(article: Article) -> None:
        try:
            kind = "articles"
            doc = client.collection(kind).document()
            doc.set(
                {
                    "title": article.content.title,
                    "subtitle": article.content.subtitle,
                    "body": article.content.body,
                    "main_image": article.content.main_image,
                    "author": article.author_name,
                    "author_picture": article.author_name,
                    "category": article.category,
                    "tags": article.tags,
                    "time_to_read": article.time_to_read,
                    "comments": article.comments,
                    "created_on": article.created_on,
                    "views": article.views,
                }
            )
        except Exception as e:
            print(e)

    @staticmethod
    def get(id) -> Union[Article, None]:
        try:
            kind = "articles"
            doc_ref = client.collection(kind).document(id)
            doc = doc_ref.get()
            if doc.exists:
                return doc.to_dict()
        except Exception as e:
            print(e)
        return None

    @staticmethod
    def get_all() -> Union[List[Union[Article, None]], None]:
        try:
            kind = "articles"
            collection = client.collection(kind)
            articles = []
            for doc in collection.stream():
                articles.append(doc.to_dict())
            return articles
        except Exception as e:
            print(e)
        return None
