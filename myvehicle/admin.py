from django.contrib import admin
from .models import Management_Data

class data(admin.ModelAdmin):
        model = Management_Data
        list_display = ['user','vehicle_number','vehicle_type','vehicle_model','vehicle_desc']
        list_per_page = 2
        list_editable = ('vehicle_number',)
        list_filter = ('vehicle_type',)
        search_fields = ('vehicle_number',)
        
admin.site.register(Management_Data,data)

# Register your models here.
