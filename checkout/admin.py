from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineAdminInline(admin.TabularInline): #Tabularline subclass defines the template used to render the Order class in the Admin Iterface
    model = OrderLineItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, ) #the admin interface has the ability to edit more than one model on a single page. This is knos as inlines.
    
admin.site.register(Order, OrderAdmin) #This register the order to the admin panel so that the order can be edited if necessary
