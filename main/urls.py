from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('sentences/',list_sentence,name='list_sentence'),
    path('edit/<int:pk>/<str:dt>',edit_sentence,name='edit_sentence'),
    # path('/add_review',modify,name="modify"),
]