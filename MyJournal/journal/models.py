from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    #ketu perdor model User te gatshem nga Django, e kam nevoje
    #te krijoj one to many relationship
    journal_text = models.TextField()
    #this will just add the time stamp when it  was created
    created_at = models.DateTimeField(auto_now_add=True)
    journal_image = models.ImageField(upload_to = 'images/',null=True, blank=True)
    
    
    
    def __str__(self):
        return f"Journal Id : {self.id} {self.journal_text} {self.created_at} "
    
    
