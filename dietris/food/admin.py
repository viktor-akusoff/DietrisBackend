from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.urls.resolvers import URLPattern
from .models import FoodItem


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    change_list_template = "admin/model_change_list.html"

    def get_urls(self) -> list[URLPattern]:
        urls = super().get_urls()
        custom_urls = [path('import-table-dialogue/', self.process_import, name='process_import'), ]
        return custom_urls + urls

    def process_import(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
        )
        return TemplateResponse(request, "admin/import_dialogue.html", context)
