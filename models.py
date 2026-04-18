from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        abstract = True


class Student(Person):
    course = models.CharField(max_length=100)


class Teacher(Person):
    subject = models.CharField(max_length=100)

from django.db import models

# Create your models here.
