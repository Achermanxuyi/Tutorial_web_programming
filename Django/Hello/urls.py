from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("Iris", views.Iris, name="Iris"),
    path("Kaori", views.Kaori, name="Kaori"),
    path("<str:name>", views.greet, name="greet")
]