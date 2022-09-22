from django.urls import path

from . import views


urlpatterns = [
    
    #keto qe shenohen me view.add jane ne fakt dunksionet ne views
    path("", views.index, name = "index"),
    path("<int:journal_id>", views.journal, name="journal"),
    path("add", views.add, name = "add"),
    path("newPage", views.newPage, name="newPage")

    
    # path("<str:name>", views.index, name = "index")
]

