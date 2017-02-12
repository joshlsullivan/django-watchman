from django.contrib import admin
from .models import Client, EmailSent

@admin.register(Client, EmailSent)
class ClientAdmin(admin.ModelAdmin):
    pass
