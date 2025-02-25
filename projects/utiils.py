from django.shortcuts import render
from projects.modules.text_similarity.predict import calculate_similarity
from projects.modules.category_detection.predict import predict

def similarity_detection(request):
    text1 = request.POST['text1']
    text2 = request.POST['text2']
    result = calculate_similarity(text1, text2)
    context = {'result': result}
    return render(request, 'projects/text-similarity.html', context=context)

def category_serializer(request):
    text = request.POST['text']
    result = predict(text)
    context = {'result': result}
    return render(request, 'projects/category-detection.html', context)