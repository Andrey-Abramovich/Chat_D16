from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from board.models import Post, Category, Respond


def index(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    respond = Respond.objects.all()
    context = {'posts': posts, 'category': category, 'respond': respond}
    return render(request, 'board/posts.html', context)



