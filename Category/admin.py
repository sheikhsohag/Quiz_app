from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug' : ('category_name',)}
    list_display = ('category_name', 'category_slug')

admin.site.register(Category,CategoryAdmin)
