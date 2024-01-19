from django.db import models
from catagory.models import Catagory

# Create your models here.
class task(models.Model):
    task_title = models.CharField(max_length=255)
    task_description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Catagory, related_name="catagories")
    
    def __str__(self):
        return self.task_title