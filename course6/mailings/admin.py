from django.contrib import admin

from mailings.models import MailSettings


@admin.register(MailSettings)
class MailSettingsAdmin(admin.ModelAdmin):
    list_display = ('message', 'start_time', 'end_time')
    list_filter = ('status',)
    search_fields = ('period',)
