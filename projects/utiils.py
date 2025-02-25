from django.shortcuts import render
from projects.modules.text_similarity.predict import calculate_similarity

def similarity_detection(request):
    text1 = request.POST['text1']
    text2 = request.POST['text2']
    result = calculate_similarity(text1, text2)
    context = {'result': result}
    return render(request, 'projects/text-similarity.html', context=context)