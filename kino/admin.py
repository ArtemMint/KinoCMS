from django.contrib import admin
from django.contrib.auth.models import Group
from register.models.client import Client


admin.site.unregister(Group)

class ClientAdmin(admin.ModelAdmin):
    model = Client



admin.site.register(Client, ClientAdmin)