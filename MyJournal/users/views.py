from re import template
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


from dataclasses import fields
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login #so the user 
#that we will create will be logged in directly



class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    #we can specify success_url or create an function
    def get_success_url(self):
        return reverse_lazy("journal1:index")


class RegisterPage(FormView):
    template_name ='users/register.html'
    form_class = UserCreationForm #in case I want to modify this 
    #form i can do it
    success_url = reverse_lazy('journal1:index')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self,*args,**kwargs): #ketu po i bej override methods
        if self.request.user.is_authenticated:
            return redirect('journal1:index')
        return super(RegisterPage,self).get(*args,**kwargs)
            
        
    

""" def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/user.html")


def login_view(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })    
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
        "message": "Logged out."
    })
     """