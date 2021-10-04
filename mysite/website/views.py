from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting


def welcome(request):
    return render(request,"website/welcome.html",
                  {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("Welcome To The Meeting Planner<br>This page was served at " + str(datetime.now()))




