from django.contrib import admin
from service.models import Order, Cost

# Register your models here.

class CostInline(admin.TabularInline):
	model = Cost
	extra = 3

class OrderAdmin(admin.ModelAdmin):
	list_display = ('address', 'status', 'date_added', 'date_end')
	list_filter = ['date_added', 'status']
	inlines = [CostInline]

class CostAdmin(admin.ModelAdmin):
	list_display = ('title', 'total_price', 'order_link')

admin.site.register(Order, OrderAdmin)
admin.site.register(Cost, CostAdmin)
