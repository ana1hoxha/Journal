from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:journal_id>", views.journal, name="journal"),
    path("<int:journal_id>/add", views.journal, name = "add")
    
 
    # path("<str:name>", views.index, name = "index")
]

