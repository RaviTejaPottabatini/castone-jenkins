from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=124)
    principal = models.CharField(max_length=124)
    location = models.CharField(max_length=124)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('basic_app:detail', kwargs = {'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=124)
    age = models.PositiveIntegerField()
    School = models.ForeignKey(School, related_name = 'student',on_delete = models.CASCADE)

    def __str__(self):

        return self.name