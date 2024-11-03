from django.shortcuts import render
import datetime

from django.http import HttpResponse


def index(request):
    current_time = datetime.datetime.now()
    return HttpResponse(
        "<html>"
        "<h1>Hello, world!</h1>"
        f"<h6>Current time: {current_time}</h6>"
        "</html>"
    )
