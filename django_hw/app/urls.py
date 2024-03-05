from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', base, name='base'),
    re_path(r'^todo_list/$', todo_list, name='todo_list'), # все задачи на странице
    re_path(r'^todo_detail/(?P<task_id>\d+)/$', todo_detail, name='todo_detail'), # подробная информация по задаче
]
