# SpecialDayReminderProject/specialdayreminders/models.py
from django.db import models
# SpecialDayReminderProject/specialdayreminders/models.py
from django.contrib.auth.models import User

class SpecialDayReminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    specialday_type = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name
from django.db import models

class FCMToken(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
