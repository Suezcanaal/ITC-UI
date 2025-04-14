
from django.contrib import admin
from .models import TrafficLog

@admin.register(TrafficLog)
class TrafficLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'direction', 'cars', 'is_emergency')
    list_filter = ('direction', 'is_emergency', 'timestamp')
    search_fields = ('direction',)
