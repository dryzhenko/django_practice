from django.urls import path
from todo.views import index, tags

urlpatterns = [
    path("", index, name="index"),
    path("tags/", tags, name="tags"),
]

app_name = "todo"
