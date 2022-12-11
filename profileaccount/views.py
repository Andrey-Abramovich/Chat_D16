from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.backends import BaseBackend

from profileaccount.forms import ProfileForm
from profileaccount.models import Profile


# Регистрируем нового пользователя стандартными методами джанго
class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'profileaccount/update.html'
    form_class = ProfileForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)


def profile_view(request):
    template_name = 'profileaccount/profile.html'
    us = Profile.objects.get(user=request.user.id)
    context = {
        'us': us,
    }
    return render(request, template_name, context)
