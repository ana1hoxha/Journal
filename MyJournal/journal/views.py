from django.http import HttpResponse
from msilib.schema import ListView
from multiprocessing import context
from django.shortcuts import render,redirect, get_object_or_404
import datetime
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from .models import Journal
from .forms import SubscribeForm
from django.views.generic.edit import UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from functools import wraps

#using decorators to check if the user is authenticated
def login_required(f):
    @wraps(f)
    def g(request, *args, **kwargs):
        if request.user.is_authenticated:
            return f(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("user1:login"))
    return g


@login_required
def index(request):
    #this is working
    journals = Journal.objects.filter(user = request.user)
    
    context = {
        "journals": journals,
        "date": datetime.date.today()
    }
    return render(request, "journals/index.html",context)


@login_required
def journal(request, journal_id):
    try:
        journal= Journal.objects.get(id=journal_id)
 
    except Journal.DoesNotExist:
        raise Http404("Journal Not found")    
    return render(request, "journals/journal.html", {
        "journal": journal,
        "date": datetime.date.today(),
    })
    
        
@login_required        
def add(request):
  if request.method == 'POST':
      try:
          form = SubscribeForm(request.POST, request.FILES)
          if form.is_valid():
              journal = form.save(commit=False)
              journal.user = request.user
              journal.journal_text = request.POST.get('journal_text')
              journal.save()
              return HttpResponseRedirect(reverse("journal1:index"))
          else:
              print("it didnt work out")
              return render(request, 'journals/add.html', {'form': form,
                                                           "date": datetime.date.today()
                                                           })
      except KeyError:
          return   HttpResponseBadRequest("Bad Request: no journal chosen")
      except Journal.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: journal does not exist")
           # if a GET (or any other method) we'll create a blank form    
  else:
      return render(request, 'journals/add.html', {'form': SubscribeForm(),
                                                   "date": datetime.date.today()
                                                
                                                   }) 
      
      
#HttpResponseRedirect: This creates a redirect to a specified URL (HTTP status code 302).
  
""" def edit(request, journal_id):
    journal_instance = get_object_or_404(Journal, id=journal_id)
    if request.method == 'POST':
        form = RenewForm(request.POST)
        if form.is_valid():
            journal_instance.journal_text = form.cleaned_data['journal_text']
            journal_instance.user = form.cleaned_data['user']
           # journal_instance.created = form.cleaned_data['created']
            journal_instance.save()
            return HttpResponseRedirect(reverse("journal1:index"))
    else:
        form = RenewForm()
        context = {
            'journal_id': journal_id,
            'form': form,
            'journal_instance': journal_instance
        }
    return render(request, 'journals/edit.html', context)
         
 """

class JournalUpdate(LoginRequiredMixin ,UpdateView):
    model = Journal
    fields = ['journal_text']
    """ fields = "__all__" """
    template_name = "journals/add.html"
    success_url= reverse_lazy('journal1:index')
    

class JournalDelete(LoginRequiredMixin , DeleteView):
    model= Journal
    fields = ['journal_text']
    """ fields = "__all__" """
    template_name = "journals/journal.html"
    success_url= reverse_lazy('journal1:index') 
    
def delete(request, journal_id):
    if 'delete_amount' in request.POST:
        object = Journal.objects.get(id=journal_id)
        object.delete()
        return HttpResponseRedirect(reverse("journal1:index"))


       