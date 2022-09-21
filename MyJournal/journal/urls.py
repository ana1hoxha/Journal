from django.urls import path

from . import views

app_name= "journal"
urlpatterns = [
    path("add", views.add, name = "add"),
    path("", views.index, name = "index")
    # path("<str:name>", views.index, name = "index")
]

