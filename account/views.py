from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from account.models import Health, User
from .forms import UserForm
from home.views import home
from meal.models import Device
from meal.views import makeMeal

# Create your views here.


def selectDevices(request, user_id):
    devices = Device.objects.all()
    # if request and request.user and request.user.id:
    #     devices=Device.objects.all()
    context = {"media_url": settings.MEDIA_URL, "devices": devices, "user_id": user_id}
    if request.POST and user_id:
        devices = request.POST.getlist("devices")
        print(devices)
        try:
            if devices:
                user = User.objects.get(id=user_id)
                user.devices.set(Device.objects.filter(id__in=devices))
                user.save()
                # return home(request)
                return redirect("/")
        except Exception as e:
            context["error"] = str(e)  # Handle exceptions that may occur during save
    return render(request, "admin/devices.html", context)


class SignUpView(CreateView):
    template_name = "admin/register.html"
    next_page = "/makeMeal/"

    def get(self, request, *args, **kwargs):
        healths = Health.objects.all()
        context = {
            "healths": healths,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        healths = Health.objects.all()
        context = {"healths": healths}
        if user_form.is_valid():  # Ensure that the form is valid before saving
            user = user_form.save(commit=False)
            user.password = make_password(request.POST["password"])
            user.is_active = True
            user.is_staff = True
            user.is_superuser = False
            try:
                user.save()
                return redirect(reverse("selectDevices", args=[user.id]))
            except Exception as e:
                context["error"] = str(
                    e
                )  # Handle exceptions that may occur during save
        else:
            context["form_errors"] = (
                user_form.errors
            )  # Include form errors in the context
        return render(request, self.template_name, context=context)


class LoginView(LoginView):
    template_name = "login.html"
    next_page = "/"

    # def get_success_url(self):
    #     with tenant_context(self.request.tenant):
    #         # return reverse_lazy("tenant_dashboard")
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context=context)


def logout_view(request):
    logout(request)
    request.user = None
    return home(request)
