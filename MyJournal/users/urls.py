from django.urls import path
from .views import CustomLoginView

app_name = "user1"
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name ="login")
] 

    
"""     path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout") """