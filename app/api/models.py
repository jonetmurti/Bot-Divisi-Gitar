from django.db import models

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