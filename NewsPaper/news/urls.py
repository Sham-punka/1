from django.urls import path
from .views import *


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
]