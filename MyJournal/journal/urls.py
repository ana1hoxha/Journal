from django.urls import path

from . import views


urlpatterns = [
    
    #keto qe shenohen me view.add jane ne fakt dunksionet ne views
    path("", views.index, name = "index"),
    path("<int:journal_id>", views.journal, name="journal"),
    path("add", views.add, name = "add"),
    path('<int:journal_id>/edit/', views.edit, name='edit')
]


    
    # path("<str:name>", views.index, name = "index")

