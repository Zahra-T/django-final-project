from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','subject','created_date')
    list_filter = ('subject','email')
    search_fields = ('name','subject','message')

admin.site.register(Contact, ContactAdmin)