from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all()

    return render(request, 'home.html', {'recipes':recipes})

def total_list(request):
    recipes = Recipe.objects.all()

    return render(request, 'total_list.html', {'recipes':recipes})

def keyword(request):
    return render(request, 'keyword.html')

def goso(request):
    recipes = Recipe.objects.all()

    return render(request, 'goso.html', {'recipes':recipes})

def sweet(request):
    recipes = Recipe.objects.all()

    return render(request, 'sweet.html', {'recipes':recipes})

def spicy(request):
    recipes = Recipe.objects.all()

    return render(request, 'spicy.html', {'recipes':recipes})

def sour(request):
    recipes = Recipe.objects.all()

    return render(request, 'sour.html', {'recipes':recipes})

def salty(request):
    recipes = Recipe.objects.all()

    return render(request, 'salty.html', {'recipes':recipes})


def detail(request, recipe_pk):
    recipe = Recipe.objects.get(pk=recipe_pk)

    return render(request, 'detail.html', {'recipe':recipe})