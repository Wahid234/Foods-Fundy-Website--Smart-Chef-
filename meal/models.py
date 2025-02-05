from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from account.models import BaseModel, User, Health

# Create your models here.


# class Tag(BaseModel):
#     """
#     Tags model
#     name: String
#     Notes: Text
#     """

#     name = models.CharField(
#         max_length=500, blank=True, null=True, verbose_name=_("Name")
#     )
#     notes = models.TextField(blank=True, null=True, verbose_name=_("Notes"))

#     def __str__(self):
#         """_summary_

#         Returns:
#             _type_: _description_
#         """
#         return self.name


class Category(BaseModel):
    name = models.CharField(
        max_length=500, blank=True, null=True, verbose_name=_("Name")
    )
    image = models.ImageField(
        max_length=500,
        upload_to="images/categories",
        blank=True,
        null=True,
        verbose_name=_("Image"),
    )
    # TYPE_CHOICES = (
    #     ("main", _("Main")),
    #     ("secondary", _("Secondary")),
    # )
    # type = models.CharField(
    #     max_length=20,
    #     blank=True,
    #     null=True,
    #     choices=TYPE_CHOICES,
    #     verbose_name=_("Type"),
    # )
    notes = models.TextField(blank=True, null=True, verbose_name=_("Notes"))

    def __str__(self):
        return self.name


class Ingredient(BaseModel):
    name = models.CharField(
        max_length=500, blank=True, null=True, verbose_name=_("Name")
    )
    health_status = models.ForeignKey(
        Health,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Health status"),
    )
    categories = models.ManyToManyField(
        Category, blank=True, null=True, related_name="ingredient_categories", verbose_name=_("Categories")
    )
    # tags = models.ManyToManyField(
    #     Tag, related_name="ingredient_tags", verbose_name=_("Tags")
    # )
    CATEGORY_TYPE_CHOICES = (
        ("Cozen", _("Cozen")),
        ("Calender", _("Calender")),
        ("Healthy", _("Healthy")),
    )
    category_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=CATEGORY_TYPE_CHOICES,
        verbose_name=_("Category type"),
    )
    TYPE_CHOICES = (
        ("Breakfast", _("Breakfast")),
        ("Lunch", _("Lunch")),
        ("Dinner", _("Dinner")),
        ("Candy", _("Candy")),
        ("Drinks", _("Drinks")),
    )
    type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=TYPE_CHOICES,
        verbose_name=_("Type"),
    )
    MEAL_TYPE_CHOICES = (
        ("Popular", _("Popular")),
        ("Arab", _("Arab")),
        ("Indian", _("Indian")),
    )
    meal_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=MEAL_TYPE_CHOICES,
        verbose_name=_("Meal type"),
    )
    image = models.ImageField(
        max_length=500,
        upload_to="images/ingredients",
        blank=True,
        null=True,
        verbose_name=_("Image"),
    )
    notes = models.TextField(blank=True, null=True, verbose_name=_("Notes"))

    def __str__(self):
        return self.name


class Device(BaseModel):
    name = models.CharField(
        max_length=500, blank=True, null=True, verbose_name=_("Name")
    )
    notes = models.TextField(blank=True, null=True, verbose_name=_("Notes"))
    image = models.ImageField(
        max_length=500,
        upload_to="images/devices",
        blank=True,
        null=True,
        verbose_name=_("Image"),
    )

    def __str__(self):
        return self.name


class Meal(BaseModel):
    name = models.CharField(
        max_length=500, blank=True, null=True, verbose_name=_("Name")
    )
    health_status = models.ForeignKey(
        Health,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Health status"),
    )
    categories = models.ManyToManyField(
        Category,blank=True, null=True, related_name="meal_categories", verbose_name=_("Categories")
    )
    # tags = models.ManyToManyField(Tag, related_name="meal_tags", verbose_name=_("Tags"))
    devices = models.ManyToManyField(
        Device, related_name="meal_devices", verbose_name=_("Devices")
    )
    ingredients = models.ManyToManyField(
        Ingredient, related_name="meal_ingredients", verbose_name=_("Ingredients")
    )
    video = models.FileField(
        upload_to='images/meals/videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mov', 'avi', 'mp4', 'mkv'])]
        , verbose_name=_("Video"),blank=True, null=True
    )
    image = models.ImageField(
        max_length=500,
        upload_to="images/meals",
        blank=True,
        null=True,
        verbose_name=_("Image"),
    )
    MEAL_TYPE_CHOICES = (
        ("Popular", _("Popular")),
        ("Arab", _("Arab")),
        ("Indian", _("Indian")),
    )
    meal_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=MEAL_TYPE_CHOICES,
        verbose_name=_("Meal type"),
    )
    CATEGORY_TYPE_CHOICES = (
        ("Cozen", _("Cozen")),
        ("Calender", _("Calender")),
        ("Healthy", _("Healthy")),
    )
    category_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=CATEGORY_TYPE_CHOICES,
        verbose_name=_("Category type"),
    )
    TYPE_CHOICES = (
        ("Breakfast", _("Breakfast")),
        ("Lunch", _("Lunch")),
        ("Dinner", _("Dinner")),
        ("Candy", _("Candy")),
        ("Drinks", _("Drinks")),
    )
    type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=TYPE_CHOICES,
        verbose_name=_("Type"),
    )
    HEALTHY_TYPE_CHOICES = (
        ("DIET", _("DIET")),
        ("KETO", _("KETO")),
    )
    healthy_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=HEALTHY_TYPE_CHOICES,
        verbose_name=_("Healthy type"),
    )
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    notes = models.TextField(blank=True, null=True, verbose_name=_("Notes"))

    def __str__(self):
        return self.name


class UserMeals(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="ums_user",
        verbose_name=_("User"),
    )
    meals = models.ManyToManyField(
        Meal, related_name="ums_meals", verbose_name=_("Meals")
    )


class UserMealIngredient(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="umi_user",
        verbose_name=_("User"),
    )
    categories = models.ManyToManyField(
        Category,
        blank=True,
        null=True,
        related_name="umi_categories",
        verbose_name=_("Categories"),
    )
    # tags = models.ManyToManyField(Tag,blank=True,null=True, related_name='umi_tags',verbose_name=_("Tags"))
    # devices = models.ManyToManyField(Device,blank=True,null=True, related_name='umi_devices',verbose_name=_("Devices"))
    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True,
        null=True,
        related_name="umi_ingredients",
        verbose_name=_("Ingredients"),
    )
    MEAL_TYPE_CHOICES = (
        ("Popular", _("Popular")),
        ("Arab", _("Arab")),
        ("Indian", _("Indian")),
    )
    meal_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=MEAL_TYPE_CHOICES,
        verbose_name=_("Meal type"),
    )
    CATEGORY_TYPE_CHOICES = (
        ("Cozen", _("Cozen")),
        ("Calender", _("Calender")),
        ("Healthy", _("Healthy")),
    )
    category_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=CATEGORY_TYPE_CHOICES,
        verbose_name=_("Category type"),
    )
    TYPE_CHOICES = (
        ("Breakfast", _("Breakfast")),
        ("Lunch", _("Lunch")),
        ("Dinner", _("Dinner")),
        ("Candy", _("Candy")),
        ("Drinks", _("Drinks")),
    )
    type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=TYPE_CHOICES,
        verbose_name=_("Type"),
    )
    HEALTHY_TYPE_CHOICES = (
        ("DIET", _("DIET")),
        ("KETO", _("KETO")),
    )
    healthy_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=HEALTHY_TYPE_CHOICES,
        verbose_name=_("Healthy type"),
    )
