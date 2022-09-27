from django.contrib import admin

from .models import Reserve, Shop

class ReserveAdmin(admin.ModelAdmin):
    
    list_display = ('reserve_date', 'reserve_time', 'name', 'reserve_num', 'email', 'tel', 'comment') 
    list_filter = ['reserve_date'] 
    search_fields = ['reserve_date'] 

class ShopAdmin(admin.ModelAdmin):
   
    fieldsets = [
            (None, {'fields': ('reservable_date',
                ('start_time', 'end_time'),
                'max_reserve_num',
            )}),
    ]

admin.site.register(Reserve, ReserveAdmin)
admin.site.register(Shop, ShopAdmin)

# Register your models here.
