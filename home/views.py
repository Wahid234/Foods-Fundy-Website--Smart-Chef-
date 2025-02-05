from django.shortcuts import render
from django.conf import settings
from meal.models import Category, Ingredient, Meal


# Create your views here.
def home(request):
    categories = Category.objects.all()
    populars = Meal.objects.filter(meal_type="Popular")
    arabs = Meal.objects.filter(meal_type="Arab")
    indians = Meal.objects.filter(meal_type="Indian")
    breakfasts = Meal.objects.filter(type="Breakfast")
    lunches = Meal.objects.filter(type="Lunch")
    dinners = Meal.objects.filter(type="Dinner")
    candies = Meal.objects.filter(type="Candy")
    drinks = Meal.objects.filter(type="Drinks")
    diets = Meal.objects.filter(healthy_type="DIET")
    ketos = Meal.objects.filter(healthy_type="KETO")
    meals = Meal.objects.all()
    if request and request.user and request.user.id:
        if request.user.health_status:
            meals = Meal.objects.filter(health_status=request.user.health_status)
    context = {
        "media_url": settings.MEDIA_URL,
        "meals": meals,
        "media_url": settings.MEDIA_URL,
        "populars": populars,
        "arabs": arabs,
        "indians": indians,
        "categories":categories,
        "breakfasts": breakfasts,
        "lunches": lunches,
        "dinners": dinners,
        "candies": candies,
        "diets": diets,
        "ketos": ketos,
        "drinks": drinks,
    }

    return render(request, "index.html", context)


def categories(request):
    categories = Category.objects.all()
    context = {
        "media_url": settings.MEDIA_URL,
        "categories":categories
    }
    return render(request, "categories.html", context)


def cozens(request):
    populars = Meal.objects.filter(meal_type="Popular")
    arabs = Meal.objects.filter(meal_type="Arab")
    indians = Meal.objects.filter(meal_type="Indian")
    context = {
        "media_url": settings.MEDIA_URL,
        "populars": populars,
        "arabs": arabs,
        "indians": indians,
    }
    return render(request, "cozens.html", context)


def calenders(request):
    breakfasts = Meal.objects.filter(type="Breakfast")
    lunches = Meal.objects.filter(type="Lunch")
    dinners = Meal.objects.filter(type="Dinner")
    candies = Meal.objects.filter(type="Candy")
    drinks = Meal.objects.filter(type="Drinks")
    context = {
        "media_url": settings.MEDIA_URL,
        "breakfasts": breakfasts,
        "lunches": lunches,
        "dinners": dinners,
        "candies": candies,
        "drinks": drinks,
    }
    return render(request, "calenders.html", context)


def healthies(request):
    diets = Meal.objects.filter(healthy_type="DIET")
    ketos = Meal.objects.filter(healthy_type="KETO")
    context = {
        "media_url": settings.MEDIA_URL,
        "diets":diets,
        "ketos":ketos,
    }
    return render(request, "healthies.html", context)
