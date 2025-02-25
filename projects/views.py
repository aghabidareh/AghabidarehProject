from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

from projects.modules.poetry.generator import generator
from projects.utiils import similarity_detection, category_serializer


@require_GET
def index(request):
    return render(request , 'projects/index.html')

@require_GET
def about_me(request):
    return render(request , 'projects/about-me.html')

@require_GET
def why(request):
    return render(request , 'projects/why.html')

@require_http_methods(['GET', 'POST'])
def text_similarity(request):
    if request.method == 'POST':
        return similarity_detection(request)
    return render(request , 'projects/text-similarity.html')

@require_http_methods(['GET', 'POST'])
def category_detection(request):
    if request.method == "POST":
        category_serializer(request)

    return render(request , 'projects/category-detection.html')

@require_http_methods(['GET', 'POST'])
def poet(request):
    if request.method == "POST":
        topic = request.POST['topic']
        result = generator(topic)
        context = {'result': result}
        return render(request, 'projects/poet.html' , context)
    return render(request, 'projects/poet.html')