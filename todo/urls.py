from django.urls import path
from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TaskStatusUpdateView,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/add/", TaskCreateView.as_view(), name="task-create"),
    path("tag/add/", TagCreateView.as_view(), name="tag-create"),
    path("task/render/<int:pk>/", TaskStatusUpdateView.as_view(), name="task-status-update"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tag/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
