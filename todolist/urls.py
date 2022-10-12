from django.urls import path
from todolist.views import add_task, delete_task, display_finished, register, login_user, logout_user, show_json, show_todolist, create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('display-finished/<int:id>/', display_finished, name='display_finished'),
    path('delete/<int:id>/', delete_task, name='delete'),
    path('json/', show_json, name='show_json'), # show current user's data
    path('add/', add_task, name='add_task'),    # post current user's data + show successfully uploaded data
]