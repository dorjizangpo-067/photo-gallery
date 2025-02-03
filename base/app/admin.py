from django.contrib import admin

# Register your models here.
from .models import User, Photos

admin.site.register(User)
admin.site.register(Photos)