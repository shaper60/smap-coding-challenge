class Breadcrumb(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url

class BreadcrumbList(object):
    def __init__(self, arr):
        self.head = Breadcrumb(arr[0]['name'], arr[0]['url'])
        self.tail = None
        self.list = []
        if len(arr) > 1:
            self.tail = Breadcrumb(arr[-1]['name'], arr[-1]['url'])
        if len(arr) > 2:
            self.list = [Breadcrumb(a['name'], a['url']) for a in arr[1:-1]]
