from django.db import models
from django.contrib.auth.models import User 

class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.station_name

class Accuser(models.Model):
    accuser_name = models.CharField(max_length=100)
    accuser_contact = models.TextField()
    
    def __str__(self):
        return self.accuser_name

class Accused(models.Model):
    accused_name = models.CharField(max_length=100)
    accused_contact = models.TextField()
    
    def __str__(self):
        return self.accused_name

class Claim(models.Model):
    accuser = models.ForeignKey(Accuser, on_delete=models.CASCADE)
    accused = models.ForeignKey(Accused, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE) 
    claim_details = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Claim by {self.Accuser.accuser_name} at {self.Station.station_name}'

class Progress(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Progress on {self.claim} at {self.date_added}'

