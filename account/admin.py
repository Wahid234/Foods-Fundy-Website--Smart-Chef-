from django.contrib import admin
from .models import User, Language, Health


# Register your models here.
@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("created_at",)
    search_fields = ("name",)


# @admin.register(Language)
# class LanguageAdmin(admin.ModelAdmin):
#     list_display = ('name','abbr')
#     list_filter = ('created_at',)
#     search_fields=('name','abbr')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        "gender",
        "health_status",
        "address",
        "notes",
        "date_joined",
    )
    list_filter = ("gender", "health_status", "devices", "date_joined")
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        "gender",
        "health_status",
        "address",
        "notes",
        "date_joined",
    )
    autocomplete_fields = ("health_status","devices",)

    # fields=["username", ("first_name", "last_name","password", "email", "phone"),("gender", "language", "health_status"),
    #         ("image", "address", "notes")]
    def get_form(self, request, obj=None, **kwargs):
        """_summary_

        Args:
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        if obj:
            current_user = request.user
            self.exclude = ()
            if not current_user.is_superuser:
                self.exclude = (
                    "is_superuser",
                    "user_permissions",
                    "password",
                    "groups",
                    "is_staff",
                    "is_active",
                )
            else:
                self.include = (
                    "is_superuser",
                    "user_permissions",
                    "groups",
                    "is_staff",
                    "is_active",
                )

        else:
            self.exclude = (
                "is_superuser",
                "user_permissions",
                "groups",
                "is_staff",
                "is_active",
            )
        form = super(UserAdmin, self).get_form(request, obj, **kwargs)
        # form. = current_user
        return form
