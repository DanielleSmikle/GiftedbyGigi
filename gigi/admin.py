from django.contrib import admin
from .models import Collection, Feature, Customer, Order, OrderItem, ShippingAddress

@admin.register(Customer)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
        list_display =['scent','description','slug','price','in_stock', 'created']
        list_filter = ['in_stock']
        list_editable = ['price', 'in_stock']
        prepopulated_fields = {'slug': ('scent',)}

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)





        

