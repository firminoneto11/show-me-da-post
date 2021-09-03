from django.urls import path
from posts.views import *

urlpatterns = [
    path('', view=home, name='home'),
    path('remove', view=remove, name='remove'),
    path('logout/', view=log_out, name='logout')
]
