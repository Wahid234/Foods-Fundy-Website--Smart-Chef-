from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

# Create your models here.


class BaseModel(models.Model):
    """
    BaseModel: Model
    created_by: Foreign
    updated_by: Foreign
    created_at: String
    updated_at: String
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    created_by = models.ForeignKey(
        "account.User",
        related_name="%(class)s_created_by",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Created By"),
    )
    updated_by = models.ForeignKey(
        "account.User",
        related_name="%(class)s_updated_by",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Updated By"),
    )

    class Meta:
        abstract = True


class Language(BaseModel):
    """
    Language model
    Name: String
    Abbr: String
    """

    name = models.CharField(max_length=500, verbose_name=_("Name"))
    abbr = models.CharField(max_length=10, verbose_name=_("Abbr"))
    is_active = models.BooleanField(
        default=True, blank=True, verbose_name=_("Is Active")
    )

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.name

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")


class Health(BaseModel):
    name = models.CharField(max_length=500, verbose_name=_("Name"))

    def __str__(self):

        return self.name

    class Meta:
        verbose_name = _("Health")
        verbose_name_plural = _("Health")


class User(AbstractUser, BaseModel):
    """
    User model
    Image: file
    Gender: Choices
    Phone: String
    Notes: Text
    """

    image = models.ImageField(
        max_length=500,
        upload_to="images/users",
        blank=True,
        null=True,
        verbose_name=_("Image"),
    )
    GENDER_CHOICES = (
        ("male", _("Male")),
        ("female", _("Female")),
    )
    gender = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=GENDER_CHOICES,
        verbose_name=_("Gender"),
    )
    health_status = models.ForeignKey(
        Health,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Health status"),
    )
    address = models.TextField(blank=True, null=True, verbose_name=_("Address"))
    phone = models.CharField(
        max_length=500, blank=True, null=True, verbose_name=_("Phone")
    )
    devices = models.ManyToManyField(
        "meal.Device",
        blank=True,
        null=True,
        related_name="user_devices",
        verbose_name=_("Devices"),
    )
    # language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True,null=True,related_name='user_language',verbose_name=_("Language"))
    notes = models.TextField(blank=True, null=True, verbose_name=_("Notes"))
    date_joined = models.DateTimeField(verbose_name=_("date joined"), auto_now_add=True)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
