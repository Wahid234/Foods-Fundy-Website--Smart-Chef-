from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.conf import settings
from meal.models import Category, Ingredient, Meal, UserMealIngredient, Device
from .forms import UserMealIngredientForm
from home.views import home


# Create your views here.
def makeMeal(request, categoryType, type):
    ingredients = Ingredient.objects.all()
    categories = Category.objects.all()
    context = {
        "categoryType": categoryType,
        "type": type,
        "ingredients": ingredients,
        "categories": categories,
    }
    if request and request.user and request.user.id:
        if request.user.health_status:
            ingredients = Ingredient.objects.filter(
                ~Q(health_status=request.user.health_status)
            )
        context["ingredients"] = ingredients
        if request.POST:
            if request.POST.get("categories") and request.POST.get("ingredients"):
                categories = request.POST.getlist("categories")
                ingredients = request.POST.getlist("ingredients")
                try:
                    if categories and ingredients:
                        if categoryType == "Cozen":
                            mType = type
                        else:
                            mType = None
                        if categoryType == "Calender":
                            cType = type
                        else:
                            cType = None
                        if categoryType == "Healthy":
                            hType = type
                        else:
                            hType = None
                        user_meal_ingredient = UserMealIngredient(
                            user_id=request.user.id,
                            meal_type=mType,
                            category_type=categoryType,
                            type=cType,
                            healthy_type=hType,
                        )
                        user_meal_ingredient.save()
                        user_meal_ingredient.categories.set(
                            Category.objects.filter(id__in=categories)
                        )
                        user_meal_ingredient.ingredients.set(
                            Ingredient.objects.filter(id__in=ingredients)
                        )
                        # return redirect("/generated_meals/")
                        return redirect(
                            reverse("generatedMeals", args=[user_meal_ingredient.id])
                        )
                except Exception as e:
                    context["error"] = str(
                        e
                    )  # Handle exceptions that may occur during save
    return render(request, "admin/make-meal.html", context=context)


def mealDetails(request,id=None):
    meal=None
    if id :
        meal=Meal.objects.get(id=id)
    context = {
        "media_url": settings.MEDIA_URL,
        "meal":meal
    }
    return render(request, "meal-details.html", context)


def generatedMeals(request, umi_id):
    meals = None
    if umi_id:
        umi = UserMealIngredient.objects.get(id=umi_id)
        meals = Meal.objects.filter(
            (
                ~Q(health_status=request.user.health_status)
                & Q(devices__in=request.user.devices.all())
                & (Q(meal_type=umi.meal_type) | Q(type=umi.type) | Q(healthy_type=umi.healthy_type))
                & Q(category_type=umi.category_type)
            )
            & (
                Q(categories__in=umi.categories.all())
                | Q(ingredients__in=umi.ingredients.all())
            )
        ).distinct()
    context = {"media_url": settings.MEDIA_URL, "meals": meals}
    return render(request, "generated-meals.html", context)


def meals(request, type, mealType=None):
    meals = None
    if type:
        if type == "Cozen" and mealType:
            meals = Meal.objects.filter(meal_type=mealType)
        elif type == "Calender" and mealType:
            meals = Meal.objects.filter(type=mealType)
        elif type == "Healthy" and mealType:
            meals = Meal.objects.filter(healthy_type=mealType)
    context = {"media_url": settings.MEDIA_URL, "meals": meals}
    return render(request, "meals.html", context)

def myMeals(request):
    meals = None
    if request.user and request.user.id:
        meals=UserMealIngredient.objects.filter(user_id=request.user.id)
    context = {"media_url": settings.MEDIA_URL, "meals": meals}
    return render(request, "my-meals.html", context)


# def selectDevices(request,umi_id):
#     devices=Device.objects.all()
#     # if request and request.user and request.user.id:
#     #     devices=Device.objects.all()
#     context = {
#         'media_url': settings.MEDIA_URL,
#         'devices':devices,
#         'umi_id':umi_id
#     }
#     if request.POST and umi_id:
#         devices = request.POST.get('devices').split(',')
#         try:
#             if devices:
#                 user_meal_ingredient = UserMealIngredient.objects.get(id=umi_id)
#                 user_meal_ingredient.devices.set(Device.objects.filter(id__in=devices))
#                 user_meal_ingredient.save()
#                 return home(request)
#         except Exception as e:
#             context['error'] = str(e)  # Handle exceptions that may occur during save
#     return render(request,'admin/devices.html',context)
