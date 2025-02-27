 # necessary imports
from django.shortcuts import render
from projects.modules.text_similarity.predict import calculate_similarity
from projects.modules.category_detection.predict import predict
from projects.modules.poetry.generator import generator

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

def category_serializer(request):
    # prepare the input
    text = request.POST['text']

    # prepare the response
    result = predict(text)

    # prepare the context
    context = {'result': result}

    # send the context
    return render(request, 'projects/category-detection.html', context)

def poetry_creator(request):
    # prepare the input
    topic = request.POST['topic']

    # prepare the response
    result = generator(topic)

    # prepare the context
    context = {'result': result}

    # send the context
    return render(request, 'projects/poet.html', context)