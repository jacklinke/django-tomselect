class ProxyRequest:
    """Used as a stand-in for a real request when obtaining the initial QuerySet for the widget"""

    def __init__(self, *args, model=None, **kwargs):
        self.model = model
        self.GET = {"q": "test", "model": self.model._meta.label_lower if self.model else ""}
        self.POST = {}
        self.method = "GET"
