from django.contrib import admin
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib import messages
from nutrition_table.load_exceptions import NutritionTableLoadError
from nutrition_table.load_context import NutritionTableContext
from nutrition_table.load_strategy import CSVStrategy, ODSStrategy, XLSStrategy, XLSXStrategy
from .models import FoodItem


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    change_list_template = "admin/model_change_list.html"

    def get_urls(self) -> list[URLPattern]:
        urls = super().get_urls()
        custom_urls = [path('import-dialogue/', self.process_import, name='process_import'), ]
        custom_urls += [path('import-table/', self.handle_uploaded_file, name='handle_uploaded_file'), ]
        return custom_urls + urls

    def process_import(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
        )
        return TemplateResponse(request, "admin/import_dialogue.html", context)

    def handle_uploaded_file(self, request):
        table = request.FILES.get('table', None)

        if table is None:
            self.message_user(request, "No file uploaded", level=messages.ERROR)
            return HttpResponseRedirect("../")

        table_address = default_storage.save(table.name, table)
        table_format = table_address.split('.')[-1]
        context = None

        if table_format == 'csv':
            context = NutritionTableContext(CSVStrategy())
        elif table_format == 'xls':
            context = NutritionTableContext(XLSStrategy())
        elif table_format == 'xlsx':
            context = NutritionTableContext(XLSXStrategy())
        elif table_format == 'ods':
            context = NutritionTableContext(ODSStrategy())

        if context is None:
            self.message_user(request, "Wrong file format", level=messages.ERROR)
            return HttpResponseRedirect("../")

        try:
            context.load_table(table_address)
        except NutritionTableLoadError:
            self.message_user(request, "Wrong file content", level=messages.ERROR)
            return HttpResponseRedirect("../")

        context.load_table_to_db()

        self.message_user(request, "Nuttrition data was succesfully uploaded!")
        return HttpResponseRedirect("../")
