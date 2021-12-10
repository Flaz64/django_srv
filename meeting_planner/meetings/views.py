from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Meeting, Room
from .forms import MeetingForm

def detail(requests, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(requests, "meetings/detail.html", {"meeting": meeting})
# Create your views here.

def rooms_list(requests):
    return render(requests, "meetings/rooms_list.html",
                  {"rooms" :Room.objects.all()})

# MeetingForm = modelform_factory(Meeting, exclude=[])

def new(requests):
    if requests.method == "POST":
        form = MeetingForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(requests, "meetings/new.html", {"form": form})