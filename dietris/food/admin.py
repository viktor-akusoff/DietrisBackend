from django.contrib import admin
from .models import FoodItem

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    change_list_template = "admin/model_change_list.html"
    pass
