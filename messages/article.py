from article_content import ArticleContent 
from datetime import datetime

class Article(object):
    content: ArticleContent
    author_name: str
    author_picture: str
    category: str
    tags: list[str]
    created_on: datetime

    def __init__(self, 
    content: ArticleContent, 
    author_name: str, 
    author_picture: str, 
    category: str,
    tags: 'list[str]',
    created_on: datetime) -> None:
        self.content = content
        self.author_name = author_name
        self.author_picture = author_picture
        self.category = category
        self.tags = tags
        self.created_on = created_on