from django.contrib import admin
from .models import Station, Accuser, Accused, Claim, Progress

class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name','station_location')
    search_fields = ('station_name','station_location')

class AccuserAdmin(admin.ModelAdmin):
    list_display = ('accuser_name','accuser_contact')
    search_fields = ('accuser_name','accuser_contact')

class AccusedAdmin(admin.ModelAdmin):
    list_display = ('accused_name','accused_contact')
    search_fields = ('accused_name','accused_contact') 

class ClaimAdmin(admin.ModelAdmin):
    list_display = ('accuser', 'accused', 'station','status','date_reported')
    search_fields = ('accuser__accuser_name', 'accused__accused_name', 'station__station_name','status')
    list_filter = ('status', 'date_reported')

class ProgressAdmin(admin.ModelAdmin):
    list_display = ('claim', 'description', 'date_added', 'updated_at', 'added_by')
    search_fields = ('claim__accuser__accuser_name', 'claim__accused__accused_name','description', 'added_by__username')
    list_filter = ('date_added', 'updated_at') 
    
admin.site.register(Station, StationAdmin)
admin.site.register(Accused, AccusedAdmin)
admin.site.register(Accuser, AccuserAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Progress, ProgressAdmin)

