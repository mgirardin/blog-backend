class ArticleContent(object):
    title: str
    subtitle: str
    body: str
    main_image: str
    
    def __init__(self, title: str, subtitle: str, body: str, main_image: str) -> None:
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.main_image = main_image
