from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class form(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return str(self.name)
    

class jobList(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    date_and_time = models.DateTimeField('expiration time (of ad)', default=timezone.now() + datetime.timedelta(days=30))
    Job_description = models.TextField(blank=True, null=True)
    Responsibility = models.TextField(blank=True, null=True)
    Vacancy = models.IntegerField()
    company_detail=models.TextField(blank=True, null=True)
    skills=models.TextField(blank=True, null=True)
    qualification=models.CharField(blank=True, null=True, max_length=100)
    sender_email=models.EmailField()

    def get_absolute_url(self):
        return reverse_lazy('web:job-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name)
    
    
class applyform(models.Model):
    job = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return str(self.name)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    dob = models.DateField(null=True, blank=True)
    hometown = models.CharField(max_length=50, blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    image = models.ImageField(upload_to="images/")
   
    # Add other fields related to the user's profile
    
    def get_update_url(self):
        return reverse('web:profile_update', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user.username

    
    def get_image(self):
        if self.image:
            return self.image.url
        return f"https://ui-avatars.com/api/?name={self.name[:2]}&background=e8572e&color=fff&size=128"