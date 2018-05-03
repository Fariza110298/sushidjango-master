from django.contrib import admin

# Register your models here.

from .models import Sponsor, Sushitype, SpisokMenu

#admin.site.register( SpisokMenu)
#admin.site.register( Sponsor)
admin.site.register( Sushitype)

# Define the admin class
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('sponsor_name', 'sponsor_kala', 'zakaz_product', 'printitya_zakaz')
    fields =[('sponsor_name', 'sponsor_kala', 'zakaz_product', 'printitya_zakaz')]

# Register the admin class with the associated model
admin.site.register(Sponsor, SponsorAdmin)

# Register the Admin classes for Book using the decorator

@admin.register(SpisokMenu)
class SpisokMenuAdmin(admin.ModelAdmin):
    list_display = ('sushiname', 'sponsor')

