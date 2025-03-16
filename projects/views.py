from django.views.decorators.http import require_GET, require_http_methods
from projects.utils.utils import Views

views = Views()

@require_GET
def index(request):
    return views.index(request)


@require_GET
def about_me(request):
    return views.about_me(request)


@require_GET
def why(request):
    return views.why(request)


@require_http_methods(['GET', 'POST'])
def text_similarity(request):
    return views.text_similarity(request)


@require_http_methods(['GET', 'POST'])
def category_detection(request):
    return views.category_detection(request)


@require_http_methods(['GET', 'POST'])
def poet(request):
    return views.poet(request)


@require_GET
def news(request):
    return views.news(request)


@require_GET
def news_page(request, slug=None):
    return views.news_page(request, slug)
