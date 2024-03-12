from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', base, name='home'),
    re_path(r'^todo_list/$', ListTodo.as_view(), name='todo_list'), # все задачи на странице
    re_path(r'^todo_detail/(?P<pk>\d+)/$', TodoDetail.as_view(), name='todo_detail'), # подробная информация по задаче
    re_path(r'^create_todo/$', CreateTodo.as_view(), name='create_todo'), # создание задачи
    re_path(r'^update_todo/(?P<pk>\d+)/$', UpdateTodo.as_view(), name='update_todo'), # редактирование задачи
    re_path(r'^delete_todo/(?P<pk>\d+)/$', DeleteTodo.as_view(), name='delete_todo'), # удаление задачи
]
