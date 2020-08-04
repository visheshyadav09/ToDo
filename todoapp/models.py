from django.db import models

# Create your models here.
# auto_now_add=True-this line just automatically adds the updated date every time
class todo(models.Model):
    text = models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
