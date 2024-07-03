# todo/admin.py

from django.contrib import admin
from .models import Todo
from myproject.admin_views import admin_site
try:
    admin.site.unregister(Todo)
except admin.sites.NotRegistered:
    pass

# Register with the custom admin site
admin.site.register(Todo)
