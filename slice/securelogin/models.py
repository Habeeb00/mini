from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

email_regex=RegexValidator(regex=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',message="Please enter a valid Email address.")
string_regex=RegexValidator(regex=r'^[a-zA-Z]+(?:\s[a-zA-Z]+)*$', message="Some special characters like (~!#^`'$|{}<>*) are not allowed.")

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True,db_index=True,validators=[email_regex])
    username=models.CharField(max_length=30,unique=True,blank=False,null=False,db_index=True)
    first_name = models.CharField(max_length=50, blank=True, null=True, validators=[string_regex])
    last_name = models.CharField(max_length=50, blank=True, null=True, validators=[string_regex])

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'

    def __str__(self):
        return self.username