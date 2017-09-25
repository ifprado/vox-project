from django.db import models
from django.forms import ModelForm

# Create your models here.

class Page(models.Model):
    question = models.CharField(max_length=100)
    ansA = models.CharField(max_length=100)
    ansB = models.CharField(max_length=100)
    ansC = models.CharField(max_length=100)
    ansD = models.CharField(max_length=100)
    ansInt = models.IntegerField()

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = [ 'question', 'ansA', 'ansB', 'ansC', 'ansD', 'ansInt']
    