from django.contrib import admin
from .models import HeatIndex


@admin.register(HeatIndex)
class HeatIndexAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'temperature', 'humidity')

