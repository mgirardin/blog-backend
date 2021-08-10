from datetime import datetime
from typing import List

from article_content import ArticleContent
from comment import Comment


class Article(object):
    content: ArticleContent
    author_name: str
    author_picture: str
    category: str
    tags: List[str]
    time_to_read: str
    comments: List[Comment]
    created_on: datetime
    views: int

    def __init__(
        self,
        content: ArticleContent,
        author_name: str,
        author_picture: str,
        category: str,
        tags: List[str],
        time_to_read: str,
        comments: List[Comment],
        created_on: datetime,
        views: int,
    ) -> None:
        self.content = content
        self.author_name = author_name
        self.author_picture = author_picture
        self.category = category
        self.tags = tags
        self.time_to_read = time_to_read
        self.comments = comments
        self.created_on = created_on
        self.views = views
