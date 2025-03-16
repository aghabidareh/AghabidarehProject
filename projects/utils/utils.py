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

    def index(self, request):
        """
        Render the index page.
        """
        return render(request, 'projects/index.html')

    def about_me(self, request):
        """
        Render the about me page.
        """
        return render(request, 'projects/about-me.html')

    def why(self, request):
        """
        Render the why page.
        """
        return render(request, 'projects/why.html')

    def text_similarity(self, request):
        """
        Handle text similarity detection.
        - GET: Render the text similarity page.
        - POST: Process the input texts and return the similarity result.
        """
        if request.method == 'POST':
            return Helpers.similarity_detection(request)
        return render(request, 'projects/text-similarity.html')

    def category_detection(self, request):
        """
        Handle category detection.
        - GET: Render the category detection page.
        - POST: Process the input text and return the detected category.
        """
        if request.method == "POST":
            return Helpers.category_serializer(request)
        return render(request, 'projects/category-detection.html')

    def poet(self, request):
        """
        Handle poetry generation.
        - GET: Render the poet page.
        - POST: Process the input topic and return the generated poetry.
            """
        if request.method == "POST":
            return Helpers.poetry_creator(request)
        return render(request, 'projects/poet.html')

    def news(self, request):
        """
        Render a list of all published news items.
        """
        result = News.all_news()
        count = News.get_news_count()
        context = {'news': result, 'count': count}
        return render(request, 'projects/news.html', context)

    def news_page(self, request, slug):
        """
        Render the details of a specific news item.
        - slug: The slug of the news item to display.
        """
        news = News.get_news_by_identifier(identifier=slug)
        context = {'news': news}
        return render(request, 'projects/news-page.html', context)
