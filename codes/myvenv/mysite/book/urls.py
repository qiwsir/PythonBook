from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_title, name="book_title"),
    url(r'(?P<article_id>\d)/$', views.book_article, name='book_content'),
]