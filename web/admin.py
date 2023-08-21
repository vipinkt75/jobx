from django.contrib import admin
from .models import form ,jobList,applyform,UserProfile
# Register your models here.

@admin.register(form)
class form(admin.ModelAdmin):
    model=form
    extra = 0
    fields = ("name","email", "subject", "message")


@admin.register(jobList)
class jobList(admin.ModelAdmin):
    list_display = ("name", "location", "jobtype", "salary", "date_and_time")   


@admin.register(applyform)
class applyform(admin.ModelAdmin):
    model=applyform
    list_display = ("name", "email", "website", "file")


   
@admin.register(UserProfile)
class profile(admin.ModelAdmin):
    model = UserProfile