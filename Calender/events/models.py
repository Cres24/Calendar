from django.db import models

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    all_day = models.BooleanField(default=False)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title