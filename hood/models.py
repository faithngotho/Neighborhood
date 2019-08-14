from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    
    neighbourhood = models.CharField(max_length=90)
    pic = models.ImageField(blank=True,upload_to = 'hoods/')
    location = models.CharField(max_length = 50,null = True)

    def __str__(self):
        return f'{self.neighbourhood}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'images/',default = 'images/beauty1.jpg')
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)
    bio = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.user.username}'


    

class HoodDetails(models.Model):
    TYPE = (
        ('Contact','Contact'),
        ('Business','Business'),
    )
    detail = models.CharField(max_length = 255)
    detailtype = models.CharField(max_length = 255,choices=TYPE)
    contact = models.CharField(max_length = 13)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'{self.detail}'


class Post(models.Model):
    post = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=False,null=False)
    image = models.ImageField(upload_to = 'images/')
    def __str__(self):
        return f'{self.user}'


class Business(models.Model):
    name = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User, null = True,related_name='user')
    neighbourhood = models.ForeignKey(Neighbourhood, null = True,related_name='business')
    class Meta:
        ordering = ['-pk']

    def save_business(self):
        self.save()

    @classmethod
    def get_business(cls, profile):
        business = Business.objects.filter(Profile__pk = profile)
        return business
    
    @classmethod
    def get_all_business(cls):
        project = Project.objects.all()
        return project

    @classmethod
    def search(cls,search_term):
        biz = cls.objects.filter(name__icontains=search_term)
        return biz