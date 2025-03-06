
# necessary imports
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods
from projects.utils.utils import similarity_detection, category_serializer, poetry_creator

# requirement
@require_GET
def index(request):
    # render the html
    return render(request , 'projects/index.html')

# requirement
@require_GET
def about_me(request):
    # render the html
    return render(request , 'projects/about-me.html')

# requirement
@require_GET
def why(request):
    # render the html
    return render(request , 'projects/why.html')

# requirement
@require_http_methods(['GET', 'POST'])
def text_similarity(request):
    if request.method == 'POST':
        # response
        return similarity_detection(request)
    # render the html
    return render(request , 'projects/text-similarity.html')

# requirement
@require_http_methods(['GET', 'POST'])
def category_detection(request):
    if request.method == "POST":
        # response
        return category_serializer(request)
    # render the html
    return render(request , 'projects/category-detection.html')

# requirement
@require_http_methods(['GET', 'POST'])
def poet(request):
    if request.method == "POST":
        # response
        return poetry_creator(request)
    # render the html
    return render(request, 'projects/poet.html')


@require_GET
def news(request):
    """
    :param request:
    :return: html page of news
    """
    return render(request, 'projects/news.html')

@require_GET
def get_news(request , pk):
    pass