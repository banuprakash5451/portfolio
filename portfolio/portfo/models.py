from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=30)
    Profile_img=models.ImageField(upload_to='img',null=True)
    bio=models.TextField()
    about=models.TextField()
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    linkedin=models.URLField()
    github=models.URLField()


class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Education(models.Model):
    degree=models.CharField(max_length=100)
    institution=models.CharField(max_length=200)
    year_of_start=models.IntegerField()
    year_of_end=models.IntegerField()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    

class Document(models.Model):
    document = models.FileField(upload_to='documents/')


class contected(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)