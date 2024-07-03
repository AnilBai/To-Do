# myproject/admin_views.py

from django.contrib.admin.models import LogEntry
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.urls import path
from django.http import HttpResponse
from django.template import loader
from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin

@staff_member_required
def clear_admin_logs(request):
    LogEntry.objects.all().delete()
    return redirect('admin:index')

# Custom admin site to add clear button in the admin index
class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('clear-logs/', self.admin_view(clear_admin_logs), name='clear_admin_logs')
        ]
        return custom_urls + urls

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        clear_logs_url = reverse('admin:clear_admin_logs')
        extra_context['clear_logs_button'] = format_html('<a class="button" href="{}">Clear Recent Actions</a>', clear_logs_url)
        return super().index(request, extra_context=extra_context)

# Instantiate the custom admin site
admin_site = CustomAdminSite()
