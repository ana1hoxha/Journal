from django.db import models

# Create your models here.
class Journal(models.Model):
    journal_text = models.CharField(max_length=64)
   

    def __str__(self):
        return f"Journal Id : {self.id} {self.journal_text}"