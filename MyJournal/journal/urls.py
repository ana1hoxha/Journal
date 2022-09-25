from django.urls import path

from . import views


urlpatterns = [
    
    #keto qe shenohen me view.add jane ne fakt dunksionet ne views
    path("<str:name>", views.index, name="name"),
    path("<str:name>/<int:journal_id>", views.journal, name="journal"),
    path("<str:name>/add", views.add, name = "add"),
    path('<str:name>/edit/', views.edit, name='edit')
]


    
    # path("<str:name>", views.index, name = "index")

