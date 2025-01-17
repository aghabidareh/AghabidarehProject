from django.urls import path
from projects.views import *

urlpatterns = [
    path('' , index , name='index'),
    path('about-me' , about_me , name='about-me'),
    path('why' , why , name='why'),
    path('text-simialrity' , text_similarity , name='text-similarity'),
    path('category-detection' , category_detection , name='category-detection'),
    path('author' , author , name='author'),
]