from django.urls import path
from . import views
from .views import  JournalUpdate


app_name = "journal1"
urlpatterns = [
    
    #keto qe shenohen me view.add jane ne fakt dunksionet ne views
    path("", views.index, name="index"),
    path("<int:journal_id>", views.journal, name="journal"),
    path("add", views.add, name = "add"),
    #path('<int:journal_id>/edit', views.edit, name='edit'),
    path('journal-update/<int:pk>', JournalUpdate.as_view(), name='journal-update'),
    path('delete/<int:journal_id>', views.delete, name='delete')
]

    # path("<str:name>", views.index, name = "index")

