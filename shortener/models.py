from django.db import models
from django.conf import settings
from . utils import update_url_details
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class UrlShortener(models.Model): 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    original_url = models.URLField()
    new_short_url = models.CharField(max_length=20, unique=True, blank=True)
    usage_count = models.IntegerField(default=0)
    lifespan = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField()


    def __str__(self):
        return '{} - {}'.format(self.created_by, self.original_url)

    
    def save(self, *args, **kwargs):
        url_obj = update_url_details(self)
        self.new_short_url = url_obj["short_url"]
        self.max_uses = url_obj["max_uses"]
        self.date_created = url_obj["date_created"]
        self.date_expired = url_obj["expiry_date"]
        
        super().save(*args, **kwargs)


class CustomUser(AbstractUser):
    """Customized user model"""

    slug            =       models.SlugField(allow_unicode=True, unique=True)
    mobile_no       =       models.CharField(max_length=10, null=True)
    profile_pic     =       models.ImageField(upload_to='media/img', null=True)


    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):

        if(self.username == 'admin'):
            """Change slug to avoid url conflict with cpanel if user is admin"""
            self.slug = 'admin_user'
        else:
            self.slug = self.username

        super().save(*args, **kwargs)