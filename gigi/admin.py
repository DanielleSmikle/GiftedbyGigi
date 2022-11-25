from django.contrib import admin

from .models import Collection, Feature

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
        list_display =['scent','description','slug','price','in_stock', 'created']
        list_filter = ['in_stock']
        list_editable = ['price', 'in_stock']
        prepopulated_fields = {'slug': ('title',)} 

