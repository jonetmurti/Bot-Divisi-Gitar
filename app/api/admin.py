from django.contrib import admin
from .models import Proker, Event, BotResponse

# Register your models here.
admin.site.register(Proker)
admin.site.register(Event)
admin.site.register(BotResponse)