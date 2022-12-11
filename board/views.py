from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from board.models import Post, Category, Respond


def index(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    respond = Respond.objects.all()
    if not User.is_anonymous:
        user = User.objects.get(username=request.user)
        context = {'posts': posts, 'category': category, 'respond': respond, 'user': user}
    else:
        context = {'posts': posts, 'category': category, 'respond': respond,}
    return render(request, 'board/posts.html', context)



