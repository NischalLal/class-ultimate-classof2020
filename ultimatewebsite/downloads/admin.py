from django.contrib import admin
from downloads.models import DownloadItem
# Register your models here.

class DownloadItemAdmin(admin.ModelAdmin):
    '''
        Admin View for DownloadItem
    '''
    list_display = ('file',)

admin.site.register(DownloadItem, DownloadItemAdmin)