from django.contrib import admin
from .models import logform
# Register your models here.


@admin.register(logform)
class logformAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
