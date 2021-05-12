from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Proker(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField('description', name='description')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'proker'

class Event(models.Model):
    name = models.CharField(max_length=200)
    proker = models.ForeignKey(Proker, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    event_type = models.CharField(max_length=200, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_event_in_days(days=1):
        start = datetime.date.today()
        end = start + datetime.timedelta(days=days)
        return Event.objects.filter(date__range=[start, end], status=False)

    @staticmethod
    def get_weekly_events():
        return Event.get_event_in_days(6)

    @staticmethod
    def get_monthly_events():
        return Event.get_event_in_days(29)

    class Meta:
        db_table = 'event'

class BotResponse(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        response = ' | '.join([self.question, self.answer])
        return response

    class Meta:
        db_table = 'botresponse'