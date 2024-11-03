from django.shortcuts import render, redirect

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


def index(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }
    return render(request, "todo/index.html", context=context)


def tags(request):
    tag = Tag.objects.all()
    context = {
        "tags": tag,
    }
    return render(request, "todo/tags.html", context=context)


def task_status_render(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("todo:index")


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:index")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "todo/task_form.html", context=context)


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:tags")
    else:
        form = TagForm()

    context = {
        "form": form,
    }

    return render(request, "todo/tag_form.html", context=context)


def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("todo:index")
    else:
        form = TaskForm(instance=task)

    context = {
        "form": form,
    }
    return render(request, "todo/task_form.html", context=context)


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("todo:index")

    context = {
        "task": task,
    }
    return render(request, "todo/task_confirm_delete.html", context=context)


def update_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("todo:tags")
    else:
        form = TagForm(instance=tag)

    context = {
        "form": form,
        "tag": tag,
    }
    return render(request, "todo/tag_form.html", context=context)


def delete_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    if request.method == "POST":
        tag.delete()
        return redirect("todo:tags")

    context = {
        "tag": tag,
    }
    return render(request, "todo/tag_confirm_delete.html", context=context)

