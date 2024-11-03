from django.urls import path
from todo.views import index

urlpatterns = [
    path("", index),
    path("tags/", index),
]

app_name = "todo"
