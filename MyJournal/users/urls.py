from django.urls import path
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView



app_name = "user1"
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name ="login"),
    path("logout/", LogoutView.as_view(next_page = 'user1:login'), name ="logout"),
    path("register/",RegisterPage.as_view(),name="register")
] 

    
"""     path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout") """