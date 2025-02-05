from django.contrib import admin
from .models import (
    Meal,
    Category,
    Ingredient,
    Device,
    UserMealIngredient,
    UserMeals,
)

# Register your models here.


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "name",
#     )
#     list_filter = ("created_at",)
#     search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = (
        "created_at",
    )
    search_fields = ("name",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "type",
    )
    list_filter = (
        "health_status",
        "categories",
        "category_type",
        "type",
        "meal_type",
        "created_at",
    )
    search_fields = ("name",)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("created_at",)
    search_fields = ("name",)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "health_status",
        "category_type",
        "type",
        "meal_type",
        "healthy_type",
        "created_at",
    )
    list_filter = (
        "health_status",
        "category_type",
        "type",
        "meal_type",
        "created_at",
        "categories",
        "devices",
        "ingredients",
        "healthy_type",
    )
    search_fields = (
        "health_status",
        "ingredients",
        "devices",
        "categories",
        "healthy_type",
        "name",
    )
    autocomplete_fields = (
        "health_status",
        "ingredients",
        "devices",
        "categories",
    )


@admin.register(UserMealIngredient)
class UserMealIngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "category_type", "type", "meal_type","healthy_type", "created_at")
    list_filter = (
        "user",
        "category_type",
        "type",
        "meal_type",
        "ingredients",
        "categories",
        "healthy_type",
        "created_at",
    )
    search_fields = (
        "user",
        "ingredients",
        "categories",
        "healthy_type",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


# @admin.register(UserMeals)
# class UserMealsAdmin(admin.ModelAdmin):
#     list_display = ("id", "user", "created_at")
#     list_filter = (
#         "user",
#         "meals",
#         "created_at",
#     )
#     search_fields = (
#         "user",
#         "meals",
#     )

#     def has_add_permission(self, request):
#         return False

#     def has_change_permission(self, request, obj=None):
#         return False

#     def has_delete_permission(self, request, obj=None):
#         return True
