from django.contrib import admin
from securelogin.models import CustomUser 
# Register your models here.

class CustomUserInterface(admin.ModelAdmin):
    list_display=('id','username','email','first_name','last_name','is_superuser')
    list_filter=('is_staff','is_superuser')

admin.site.register(CustomUser,CustomUserInterface)