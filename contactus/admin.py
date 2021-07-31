from django.contrib import admin
from .models import ContactUs
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'phoneNumber', 'message', 'date_created')
   search_fields = ['name','email', 'phoneNumber', 'message', 'date_created' ]
   ordering = ['-date_created',]

admin.site.register(ContactUs, AuthorAdmin)