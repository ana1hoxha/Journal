from django.forms import ModelForm
from journal.models import Journal
from django import forms


class SubscribeForm(ModelForm):
    class Meta:
        model = Journal
        fields = ["journal_text"]  
        
        
class RenewForm(ModelForm):
    def clean_text(self):
        data = self.cleaned_data['journal_text']
        return data
    class Meta:
        model =  Journal
        fields = ["journal_text"]    
        

""" class RenewForm(forms.Form):
    renewal_text = forms.CharField(max_length=64)
    
    def clean_renewal_text(self):
        data = self.cleaned_data["renewal_text"]
        return data
    
    #There are two important things to note. The first is that we get our data using 
    # self.cleaned_data['renewal_date'] and that we return this data whether 
    # or not we change it at the end of the function """