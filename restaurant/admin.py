from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from restaurant.models import DishType, Ingredient, Cook, Dish


@admin.register(Cook)
class AdminCook(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ("name", "description", "ingredients")
    list_display = ("name", "dish_type", "price")
    list_filter = ("dish_type",)
    prefetch_related = ("ingredients", "cooks")

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related(
            "ingredients",
            "cooks"
        )


admin.site.register(DishType)
admin.site.register(Ingredient)
