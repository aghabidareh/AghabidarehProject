from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Index')

def about_me(request):
    return HttpResponse('About me')

def why(request):
    return HttpResponse('Why')

def text_similarity(request):
    return HttpResponse('Text Similarity')

def category_detection(request):
    return HttpResponse('Category Detection')

def author(request):
    return HttpResponse('Author')