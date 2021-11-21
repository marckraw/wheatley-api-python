from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add_todo),
    path('<int:todo_id>', views.show_todo)
]
