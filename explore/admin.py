from django.contrib import admin
from .models import Inquiry, TransportRequest


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "travelers", "travel_date", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)


@admin.register(TransportRequest)
class TransportRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "pickup", "destination", "pickup_date", "passengers", "created_at")
    search_fields = ("name", "email", "pickup", "destination")
