from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _ 




class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('email address'),max_length=254,unique=True, null=True)
    #avtar = models.ImageField(upload_to='thumbpath', blank=True)
    mobile_no = models.CharField(max_length=15)   

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'
