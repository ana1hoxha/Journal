from django.forms import ModelForm
from journal.models import Journal


class SubscribeForm(ModelForm):
    class Meta:
        model = Journal
        fields = ["journal_text"]  