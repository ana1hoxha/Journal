from multiprocessing import context
from django.shortcuts import render, get_object_or_404
import datetime
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Journal
from .forms import SubscribeForm, RenewForm



# Create your views here.


def index(request, name):
    return render(request, "journals/index.html",  {
        "journals": Journal.objects.all(),
        "name": name
    })


def journal(request, name, journal_id):
    try:
        journal= Journal.objects.get(id=journal_id)
    except Journal.DoesNotExist:
        raise Http404("Journal Not found")    
    return render(request, "journals/journal.html", {
        "journal": journal,
        "date": datetime.date.today(),
        "name":name
        
    })
    
        
def add(request, name):
  if request.method == 'POST':
      try:
          form = SubscribeForm(request.POST)
          if form.is_valid():
              journal = form.save(commit=False)
              journal.journal_text = request.POST.get('journal_text')
              journal.save()
              return HttpResponseRedirect(reverse("index", args=(name,)))
          else:
              print("it didnt work out")
              return render(request, 'journals/add.html', {'form': form,
                                                           "date": datetime.date.today(),
                                                           "name": name
                                                           })
      except KeyError:
          return   HttpResponseBadRequest("Bad Request: no journal chosen")
      except Journal.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: journal does not exist")
           # if a GET (or any other method) we'll create a blank form    
  else:
      return render(request, 'journals/add.html', {'form': SubscribeForm(),
                                                   "date": datetime.date.today(),
                                                   "name": name
                                                
                                                   }) 
      
      
#HttpResponseRedirect: This creates a redirect to a specified URL (HTTP status code 302).
   
def edit(request,name, journal_id):
    journal_instance = get_object_or_404(Journal, id=journal_id)
    if request.method == 'POST':
        form = RenewForm(request.POST)
        if form.is_valid():
            journal_instance.journal_text = form.cleaned_data['journal_text']
            journal_instance.save()
            return HttpResponseRedirect(reverse("index",args=(name,)))
    else:
        form = RenewForm()
        context = {
            'journal_id': journal_id,
            'form': form,
            'journal_instance': journal_instance,
            'name': name
        }
    return render(request, 'journals/edit.html', context)
         
