from datetime import datetime
from django.db import models
from django.forms import ModelForm

# Create your models here.
class Journal(models.Model):
    journal_text = models.CharField(max_length=64)

    def __str__(self):
        return f"Journal Id : {self.id} {self.journal_text}"
    
    
class SubscribeForm(ModelForm):
    class Meta:
        model = Journal
        fields = ["journal_text"]  