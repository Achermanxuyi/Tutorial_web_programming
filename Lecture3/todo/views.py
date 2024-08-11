from django.shortcuts import redirect, render
from django import forms

tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(request, "todo/index.html", {
        "todo": tasks
    })

# Add a new task
def add_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return redirect("todo:index")
        else:
            return render(request, "todo/add.html", {
                "form": form
            })

    return render(request, "todo/add.html", {
        "form": NewTaskForm
    })