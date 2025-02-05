"""
URL configuration for FoodsFundyWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from account.views import LoginView, SignUpView, logout_view, selectDevices
from home.views import home, categories, cozens, calenders, healthies
from meal.views import makeMeal, mealDetails, generatedMeals, meals,myMeals

urlpatterns = [
    path("admin/register/", SignUpView.as_view(), name="register"),
    path("admin/makeMeal/<str:categoryType>/<str:type>/", makeMeal, name="makeMeal"),
    path("admin/selectDevices/<int:user_id>/", selectDevices, name="selectDevices"),
    path("admin/", admin.site.urls),
    path("", home, name="index"),
    path("admin/login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("categories/", categories, name="categories"),
    path("cozens/", cozens, name="cozens"),
    path("calenders/", calenders, name="calenders"),
    path("healthies/", healthies, name="healthies"),
    path("mealDetails/<int:id>/", mealDetails, name="mealDetails"),
    path("generatedMeals/<int:umi_id>/", generatedMeals, name="generatedMeals"),
    path("meals/<str:type>/", meals, name="mealsType"),
    path("meals/<str:type>/<str:mealType>/", meals, name="mealsTypeWithMealType"),
    path("myMeals/", myMeals, name="userGeneratedMeals"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
