from django.shortcuts import render
from projects.modules.category_detection.predict import predict

def index(request):
    return render(request , 'projects/index.html')

def about_me(request):
    return render(request , 'projects/about-me.html')

def why(request):
    return render(request , 'projects/why.html')

def text_similarity(request):
    return render(request , 'projects/text-similarity.html')

def category_detection(request):
    if request.method == "POST":
        text = request.POST['text']
        result = predict(text)
        context = {'result': result}
        return render(request, 'projects/category-detection.html' , context)

    return render(request , 'projects/category-detection.html')

def summerzie(request):
    return render(request, 'projects/poet.html')