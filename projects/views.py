from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods
from projects.utils.utils import Views

views = Views()

@require_GET
def index(request):
    """
    Render the index page.
    """
    return render(request, 'projects/index.html')


@require_GET
def about_me(request):
    """
    Render the about me page.
    """
    return render(request, 'projects/about-me.html')


@require_GET
def why(request):
    """
    Render the why page.
    """
    return render(request, 'projects/why.html')


@require_http_methods(['GET', 'POST'])
def text_similarity(request):
    """
    Handle text similarity detection.
    - GET: Render the text similarity page.
    - POST: Process the input texts and return the similarity result.
    """
    return views.text_similarity_view(request)


@require_http_methods(['GET', 'POST'])
def category_detection(request):
    """
    Handle category detection.
    - GET: Render the category detection page.
    - POST: Process the input text and return the detected category.
    """
    return views.category_detection_view(request)


@require_http_methods(['GET', 'POST'])
def poet(request):
    """
    Handle poetry generation.
    - GET: Render the poet page.
    - POST: Process the input topic and return the generated poetry.
    """
    return views.poet_view(request)


@require_GET
def news(request):
    return views.news_view(request)


@require_GET
def news_page(request, slug=None):
    return views.news_page_view(request, slug)
