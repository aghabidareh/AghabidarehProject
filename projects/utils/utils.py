# necessary imports
from django.shortcuts import render

from projects.models import News
from projects.modules.text_similarity.predict import calculate_similarity
from projects.modules.category_detection.predict import predict
from projects.modules.poetry.generator import generator

class Helpers:
    @staticmethod
    def similarity_detection(request):
        # process the inputs
        text1 = request.POST['text1']
        text2 = request.POST['text2']

        # prepare the response
        result = calculate_similarity(text1, text2)

        # prepare the context
        context = {'result': result}

        # send the context
        return render(request, 'projects/text-similarity.html', context=context)

    @staticmethod
    def category_serializer(request):
        # prepare the input
        text = request.POST['text']

        # prepare the response
        result = predict(text)

        # prepare the context
        context = {'result': result}

        # send the context
        return render(request, 'projects/category-detection.html', context)

    @staticmethod
    def poetry_creator(request):
        # prepare the input
        topic = request.POST['topic']

        # prepare the response
        result = generator(topic)

        # prepare the context
        context = {'result': result}

        # send the context
        return render(request, 'projects/poet.html', context)

class Views:
    def text_similarity_view(self , request):
        if request.method == 'POST':
            return similarity_detection(request)
        return render(request, 'projects/text-similarity.html')

    def category_detection_view(self , request):
        if request.method == "POST":
            return category_serializer(request)
        return render(request, 'projects/category-detection.html')

    def poet_view(self , request):
        if request.method == "POST":
            return poetry_creator(request)
        return render(request, 'projects/poet.html')

    def news_view(self , request):
        result = News.all_news()
        count = News.get_news_count()
        context = {'news': result, 'count': count}
        return render(request, 'projects/news.html', context)

    def news_page_view(self , request , slug):
        news = News.get_news_by_identifier(identifier=slug)
        context = {'news': news}
        return render(request, 'projects/news-page.html', context)