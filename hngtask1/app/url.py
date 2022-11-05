from django.urls import path
from .views import (TaskApiView,)


urlpatterns = [
   # path('', views.index, name='index'),
    path('app', TaskApiView.as_view())
]