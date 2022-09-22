from django.shortcuts import render
import datetime
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Journal


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
        "journal": journal
    })   


def add(request, journal_id):
    if request.method == "POST":
        try:
            journal = Journal.objects.get(pk=journal_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no journal chosen")
        except Journal.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: journal does not exist")

        return HttpResponseRedirect(reverse("journal", args=(journal_id,)))
       