from django.db import models


class Inquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    travelers = models.PositiveSmallIntegerField(default=2)
    travel_date = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.created_at:%d %b %Y}"


class TransportRequest(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    pickup = models.CharField(max_length=180)
    destination = models.CharField(max_length=180)
    pickup_date = models.DateField()
    pickup_time = models.TimeField(null=True, blank=True)
    passengers = models.PositiveSmallIntegerField(default=2)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pickup} → {self.destination} ({self.name})"
