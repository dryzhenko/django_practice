import datetime
from django.http import HttpResponse
from django.shortcuts import render
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
