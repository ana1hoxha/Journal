from socket import fromshare
from django.forms import ModelForm
from django import forms
from journal.models import Journal

class SubscribeForm(ModelForm):
    class Meta:
        model = Journal
        #fields = "__all__"
        fields = ["journal_text","journal_image"]  
        
    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['journal_image'].required = False    
        
        
        
""" class RenewForm(ModelForm):
    def clean_text(self):
        data = self.cleaned_data['journal_text']
        return data
    
    class Meta:
        model =  Journal
        fields = "__all__"
        #fields = ["journal_text"]   """  
        


""" class RenewForm(forms.Form):
    renewal_text = forms.CharField(max_length=64)
    
    def clean_renewal_text(self):
        data = self.cleaned_data["renewal_text"]
        return data """
    
    #There are two important things to note. The first is that we get our data using 
    # self.cleaned_data['renewal_date'] and that we return this data whether 
    # or not we change it at the end of the function """