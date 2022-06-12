from django.contrib import admin
from . models import UrlShortener, CustomUser

# Register your models here.
admin.site.register(UrlShortener)
admin.site.register(CustomUser)
