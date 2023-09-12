from django.db import models


class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name='email')
    first_name = models.CharField(max_length=100, verbose_name='фамилия')
    last_name = models.CharField(max_length=100, verbose_name='имя')
    surname = models.CharField(max_length=100, verbose_name='отчество')
    comment = models.TextField(blank=True, verbose_name='комментарий')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.surname} - {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailings(models.Model):
    PERIOD_CHOICES = (('day', 'Раз в день'), ('week', 'Раз в неделю'), ('month', 'Раз в месяц'))
    time_start = models.DateTimeField(auto_now_add=True)
    period = models.CharField(max_length=50, choices=PERIOD_CHOICES, verbose_name='периодичность рассылки')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="get_client", verbose_name='клиент')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    message = models.TextField(verbose_name='сообщение')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Logs(models.Model):
    date_attempt = models.DateTimeField()
    status = models.BooleanField(default=False, verbose_name="статус попытки")
    answer_server = models.TextField()
    mailings = models.ForeignKey(Mailings, on_delete=models.CASCADE, related_name="get_mailings", verbose_name='рассылка')
