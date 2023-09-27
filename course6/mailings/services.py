from datetime import datetime, timezone
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail

from mailings.models import Logs, MailSettings
import logging

logger = logging.getLogger(__name__)


def send_email(mail_settings):
    clients = mail_settings.client.all()
    clients_list = [client.email for client in clients]

    server_response = None
    status = Logs.STATUS_FAILED

    try:
        letter = send_mail(
            subject=mail_settings.message.title,
            message=mail_settings.message.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=clients_list,
        )

        if letter:
            status = Logs.STATUS_SUCCESS
            server_response = "Рассылка отправлена успешно"

    except SMTPException as e:
        server_response = str(e)
        logger.error(f"SMTPException occurred: {e}")
    else:
        logger.info("Рассылка отправлена успешно")

    if server_response:
        logger.info(f"Server response: {server_response}")

    Logs.objects.create(
        status=status,
        mailings=mail_settings,
        answer_server=server_response
    )
    print(mail_settings)


def my_job():
    now = datetime.now().timestamp()
    print("вызвали")

    for mail_settings in MailSettings.objects.filter(status=MailSettings.STATUS_IN_PROCESS):
        if (now > mail_settings.start_time.timestamp()) and (now < mail_settings.end_time.timestamp()):
            print('Попадаем в период')
            for mail_client in mail_settings.client.all():
                print(mail_client)
                mailing_log = Logs.objects.filter(mailings=mail_settings)

                if mailing_log.exists():
                    print('log exists')
                    last_try_date = mailing_log.order_by('-last_try').first().last_try
                    mail_period = mailing_log[0]
                    print(mail_period)

                    if mail_period == MailSettings.PERIOD_DAILY:
                        print('dayly')
                        if (now - last_try_date).days >= 1:
                            send_email(mail_settings)
                    elif mail_period == MailSettings.PERIOD_WEEKLY:
                        print('weekly')
                        if (now - last_try_date).days >= 7:
                            send_email(mail_settings)
                    elif mail_period == MailSettings.PERIOD_MONTHLY:
                        print('monthly')
                        if (now - last_try_date).days >= 30:
                            send_email(mail_settings)
                else:
                    print('no logs')
                    send_email(mail_settings)
