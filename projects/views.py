from django.shortcuts import render

def index(request):
    return render(request , 'projects/index.html')

def about_me(request):
    return render(request , 'projects/about-me.html')

def why(request):
    return render(request , 'projects/why.html')

def text_similarity(request):
    return render(request , 'projects/text-similarity.html')

def category_detection(request):
    return render(request , 'projects/category-detection.html')

def author(request):
    return render(request , 'projects/author.html')