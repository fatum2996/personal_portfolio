from django.db import models
import datetime

# Create your models here.
class Blog_record(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    data = models.DateField(default=datetime.date.today())
