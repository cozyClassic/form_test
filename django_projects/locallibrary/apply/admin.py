from django.contrib import admin

from .models import apply_inform

admin.site.register(apply_inform)

class apply_inform_admin(admin.ModelAdmin) :
    list_display = ('고객명','고객주소')
    fields = ['customer_name', 'customer_address']
# Register your models here.
