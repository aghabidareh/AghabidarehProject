# necessary imports
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods
from projects.models import News
from projects.utils.utils import similarity_detection, category_serializer, poetry_creator


@require_GET
def index(request):
    """
    :param request:
    :return: index page
    """
    return render(request, 'projects/index.html')


@require_GET
def about_me(request):
    """
    :param request:
    :return: about me page
    """
    return render(request, 'projects/about-me.html')


@require_GET
def why(request):
    """
    :param request:
    :return: why page
    """
    return render(request, 'projects/why.html')


@require_http_methods(['GET', 'POST'])
def text_similarity(request):
    """
    :param request: text1 and text2 , type : POST
    :return: text similarity page or the similarity between text1 and text2
    """
    if request.method == 'POST':
        return similarity_detection(request)
    return render(request, 'projects/text-similarity.html')


@require_http_methods(['GET', 'POST'])
def category_detection(request):
    """
    :param request: text, type : POST
    :return: category detection page or the category of input text
    """
    if request.method == "POST":
        return category_serializer(request)
    return render(request, 'projects/category-detection.html')


@require_http_methods(['GET', 'POST'])
def poet(request):
    """
    Handle poetry generation.
    - GET: Render the poet page.
    - POST: Process the input topic and return the generated poetry.
    """
    if request.method == "POST":
        return poetry_creator(request)
    return render(request, 'projects/poet.html')


@require_GET
def news(request):
    """
    Render a list of all published news items.
    """
    result = News.all_news()
    context = {'news': result}
    return render(request, 'projects/news.html', context)


@require_GET
def news_page(request, slug=None):
    """
    Render the details of a specific news item.
    - slug: The slug of the news item to display.
    """
    news = News.get_news_by_identifier(identifier=slug)
    context = {'news': news}
    return render(request, 'projects/news-page.html', context)
