from django.urls import path
from todo.views import index, tags, add_task, add_tag, task_status_render, update_task, delete_task, update_tag, delete_tag

urlpatterns = [
    path("", index, name="index"),
    path("tags/", tags, name="tags"),
    path('task/add/', add_task, name="add_task"),
    path('tag/add/', add_tag, name="add_tag"),
    path('task/render/<int:task_id>/', task_status_render, name="task_status_render"),
    path("task/update/<int:task_id>/", update_task, name="update_task"),
    path("task/delete/<int:task_id>/", delete_task, name="delete_task"),
    path("tag/update/<int:tag_id>/", update_tag, name="update_tag"),
    path("tag/delete/<int:tag_id>/", delete_tag, name="delete_tag"),
]

app_name = "todo"
