from django.urls import path
from posts.views import *

urlpatterns = [
    path('', view=home, name='home')
]
