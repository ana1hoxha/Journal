from django.shortcuts import render
import datetime
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

class NewJournalForm(forms.Form):
    journal = forms.CharField(label="new Journal")


def index(request):
    if "journals" not in request.session:
        request.session["journals"] = []
    return render(request, "journal/index.html",  {
        # "name": name.capitalize(),
        "journals": request.session["journals"]
    })


def add(request):
    if request.method == "POST":  # this means i submitted the form
        form = NewJournalForm(request.POST)
        if form.is_valid():
            journal = form.cleaned_data["journal"]
            request.session["journals"] += [journal]
            print(request.session["journals"])
            return HttpResponseRedirect(reverse("journal:index"))
        else:
            return render(request, "journal/add.html", {
            "form": form,
            "date": datetime.date.today()
        })

    return render(request, "journal/add.html", {
        "form": NewJournalForm(),
        "date": datetime.date.today()
    })
