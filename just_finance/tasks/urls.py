from django.urls import path, include

from . import views

app_name = "todos"

urlpatterns = [
path("add", views.add_todo),
path("list", views.list_todos),
path("save", views.save_nota),
path("mostra", views.mostra_nota),
path("delete_notes", views.delete_notes),
]