from django.urls import path
from .views import *

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('<int:store_id>/',detail, name='detail'),
    path('create/',create, name='create'),
]
