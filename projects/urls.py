from django.urls import path
from projects.views import *

app_name = 'projects'

urlpatterns = [
    # index page
    path('', index, name='index'),

    # about me page
    path('about-me', about_me, name='about-me'),

    # why page
    path('why', why, name='why'),

    # similarity between two textx project page
    path('project/text-similarity', text_similarity, name='text-similarity'),

    # persian text category detection project page
    path('project/category_detection', category_detection, name='category_detection'),

    # poetry project page
    path('project/poet', poet, name='poet'),

    # news page
    path('news', news, name='news'),

    # the news page
    path('news/<slug:slug>', news_page, name='news-page'),
]
