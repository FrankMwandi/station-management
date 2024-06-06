from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.station_name

    class Meta:
        verbose_name = "Station"
        verbose_name_plural = "Stations"
        ordering = ['station_name']

class Accuser(models.Model):
    accuser_name = models.CharField(max_length=100)
    accuser_contact = models.TextField()
    accuser_location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.accuser_name

    class Meta:
        verbose_name = "Accuser"
        verbose_name_plural = "Accusers"
        ordering = ['accuser_name']

class Accused(models.Model):
    accused_name = models.CharField(max_length=100)
    accused_contact = models.TextField()
    accused_location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.accused_name

    class Meta:
        verbose_name = "Accused"
        verbose_name_plural = "Accused"
        ordering = ['accused_name']

class Claim(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('solved', 'Solved'),
        ('stagnant', 'Stagnant'),
    ]
    
    accuser = models.ForeignKey(Accuser, on_delete=models.CASCADE)
    accused = models.ForeignKey(Accused, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    claim_details = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    
    def __str__(self):
        return f'Claim by {self.accuser.accuser_name} at {self.station.station_name}'

    class Meta:
        verbose_name = "Claim"
        verbose_name_plural = "Claims"
        ordering = ['-date_reported']

class Progress(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Progress on {self.claim} at {self.date_added}'

    class Meta:
        verbose_name = "Progress"
        verbose_name_plural = "Progress"
        ordering = ['-date_added', '-updated_at']
