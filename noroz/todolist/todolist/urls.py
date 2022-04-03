from django.urls import path
from . import views

app_name = "todolist"
urlpatterns = [
    path('',views.all_todo,name="todos"),
    path('<int:id>/',views.todo_detail,name="detail")
]
