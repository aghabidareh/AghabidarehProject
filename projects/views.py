from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods
from projects.utils.utils import Views


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
    return Views.text_similarity_view(request)


@require_http_methods(['GET', 'POST'])
def category_detection(request):
    """
    Handle category detection.
    - GET: Render the category detection page.
    - POST: Process the input text and return the detected category.
    """
    return Views.category_detection_view(request)


@require_http_methods(['GET', 'POST'])
def poet(request):
    """
    Handle poetry generation.
    - GET: Render the poet page.
    - POST: Process the input topic and return the generated poetry.
    """
    return Views.poet_view(request)


@require_GET
def news(request):
    """
    Render a list of all published news items.
    """
    return news_view(request)


@require_GET
def news_page(request, slug=None):
    """
    Render the details of a specific news item.
    - slug: The slug of the news item to display.
    """
    return news_page_view(request, slug)
