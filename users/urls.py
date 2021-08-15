from django.urls import path
from users.views import *

urlpatterns = [
    path('login/', view=login, name='login'),
    path('sign_in/', view=sign_in, name='sign_in')
]
