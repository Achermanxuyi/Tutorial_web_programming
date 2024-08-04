from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "todo/index.html", {
        "todo": tasks
    })

# Add a new task
def add_task(request):
    return render(request, "todo/add.html")