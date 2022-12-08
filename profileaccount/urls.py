from django.urls import path, include

from profileaccount.views import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),

]