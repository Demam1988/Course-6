from django.urls import path

from .apps import MailingsConfig
from .views import *

app_name = MailingsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('contacts/', ContactFormView.as_view(), name='contacts'),

    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('message/list', MessageListView.as_view(), name='message_list'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),

    path('list/', MailSettingsListView.as_view(), name='list'),
    path('create/', MailSettingsCreateView.as_view(), name='create'),
    path('update/<int:pk>', MailSettingsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MailSettingsDeleteView.as_view(), name='delete'),

    path('mail_settings_status_update/<int:pk>/', StatusMailingSettingsUpdateView.as_view(),
         name='mail_settings_status_update'),

    path('mailing_log/<int:pk>/', MailingLogListView.as_view(), name='mail_log'),

    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
