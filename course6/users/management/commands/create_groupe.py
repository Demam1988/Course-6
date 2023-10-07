from django.core.management.base import BaseCommand

from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from users.models import User
from mailings.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):

        managers_group, created = Group.objects.get_or_create(name="Managers")
        content_type = ContentType.objects.get_for_model(User)
        user_permission = Permission.objects.filter(content_type=content_type)
        for perm in user_permission:
            if perm.codename == 'set_is_active':
                managers_group.permissions.add(perm)
        content_type = ContentType.objects.get_for_model(MailSettings)
        mailings_permission = Permission.objects.filter(content_type=content_type)
        for perm in mailings_permission:
            if perm.codename == 'set_status':
                managers_group.permissions.add(perm)







