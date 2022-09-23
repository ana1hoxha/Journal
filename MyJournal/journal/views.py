from django.shortcuts import render
import datetime
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Journal, SubscribeForm
from django.forms import ModelForm


# Create your views here.


def index(request):
    return render(request, "journals/index.html",  {
        # "name": name.capitalize(),
        "journals": Journal.objects.all()
    })


def journal(request, journal_id):
    try:
        journal= Journal.objects.get(id=journal_id)
    except Journal.DoesNotExist:
        raise Http404("Journal Not found")    
    return render(request, "journals/journal.html", {
        "journal": journal,
        "date": datetime.date.today()
    })
    

""" def add(request):
   if request.method == "POST":
        try:
            
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no journal chosen")
        except Journal.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: journal does not exist")

        return HttpResponseRedirect(reverse("index")) """
    
    
def add(request):
  if request.method == 'POST':
      try:
          form = SubscribeForm(request.POST)
          if form.is_valid():
              """ journal_textNew= form.cleaned_data["journal_form"]
              journal = Journal(journal_text = journal_textNew)
              journal.save() """
              form.save()
              return HttpResponseRedirect(reverse("index"))
          else:
              return render(request, 'journals/add.html', {'form': form})
      except KeyError:
          return   HttpResponseBadRequest("Bad Request: no journal chosen")
      except Journal.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: journal does not exist")
           # if a GET (or any other method) we'll create a blank form    
  else:
      return render(request, 'journals/add.html', {'form': SubscribeForm()}) 

   

""" def newPage(request):
   return render(request, "journals/newPage.html", {
       "date": datetime.date.today()
   }
    ) """
   
   
   
   