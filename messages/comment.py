from __future__ import annotations

from datetime import datetime
from typing import List


class Comment(object):
    author: str
    body: str
    created_on: datetime
    replies: List[Comment]

    def __init__(
        self, author: str, body: str, created_on: datetime, replies: List[Comment]
    ) -> None:
        self.author = author
        self.body = body
        self.created_on = created_on
        self.replies = replies
