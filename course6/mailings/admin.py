from django.contrib import admin

from mailings.models import MailSettings, Logs


@admin.register(MailSettings)
class MailSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'message')
    list_filter = ('status',)
    search_fields = ('period',)


@admin.register(Logs)
class MailSettingsAdmin(admin.ModelAdmin):
    list_display = ('last_try', 'mailings')
    list_filter = ('status',)
    search_fields = ('period',)
