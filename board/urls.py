from django.urls import path

from board.views import index

urlpatterns = [
    path('posts/', index, name='index')
]