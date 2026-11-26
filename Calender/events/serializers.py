from rest_framework import serializers
from .models import CalendarEvent

class CalendarEventSerializer(serializers.ModelSerializer):
    # Convert MongoDB ObjectId to string for JSON serialization
    id = serializers.CharField(read_only=True)
    allDay = serializers.BooleanField(source='all_day', required=False)

    class Meta:
        model = CalendarEvent
        fields = ['id', 'title', 'start', 'end', 'allDay', 'description']