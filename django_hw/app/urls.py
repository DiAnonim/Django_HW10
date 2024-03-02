from django.urls import path, re_path
from .views import *


urlpatterns = [
    # path('', home, name='home'),
    path('', base, name='base'),
    path('todo_list/', todo_list, name='todo_list'),
    re_path(r'^todo_detail/(?P<task_id>\d+)/$', todo_detail, name='todo_detail'),
]
