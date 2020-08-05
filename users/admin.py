from django.contrib import admin
from .models import  Profile,Comment,Subscription
# Register your models here.
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Subscription)