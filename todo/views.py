from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "task_list"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


class TaskStatusUpdateView(generic.UpdateView):
    model = Task
    fields = ["completed"]
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag_list")
