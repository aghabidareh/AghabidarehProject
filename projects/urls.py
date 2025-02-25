from django.urls import path
from projects.views import index , about_me , why , text_similarity , category_detection , poet

urlpatterns = [
    path('' , index , name='index'),
    path('about-me' , about_me , name='about-me'),
    path('why' , why , name='why'),
    path('project/text-similarity' , text_similarity , name='text-similarity'),
    path('project/category_detection' , category_detection , name='category_detection'),
    path('project/poet' , poet , name='poet'),
]