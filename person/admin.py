from django.contrib import admin
from .models import PersonModel

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    exclude = []
    readonly_fields = ("age",)
    fieldsets = (
        ("Personal Data", {
            "fields": (
                ("first_name", "last_name"), ("age")
            ),
        }),
    )
    list_display = ("id", "first_name", "last_name", "age")
    search_fields = ("id", "last_name")


admin.site.register(PersonModel, PersonAdmin)
