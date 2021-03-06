from django.shortcuts import render, render_to_response
from gaming_patrada.models import *
from django.shortcuts import redirect
from alphapagainator import *


# Create your views here.
def takehome(response):
    return redirect('/gaming/')


def home(request):
    games = Games.objects.all().order_by('?')[:9]
    slideshow = Games.objects.all().order_by('?')[:3]
    categories = Category.objects.all
    gamesearch = Games.objects.all()

    context = {'all_games': games, 'slideshow': slideshow, 'categories': categories, 'gamesearch': gamesearch}
    return render(request, template_name='gamingpatrada/home.html', context=context)


def category(request, category_name_slug):
    context = {}
    try:
        # bar on top mot important
        categories = Category.objects.all
        context['categories'] = categories
        # bar on top mot important


        category = Category.objects.get(slug=category_name_slug)
        context['category_name'] = category.name
        games_list = Games.objects.filter(category=category)
        context['games'] = games_list
        context['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, template_name='gamingpatrada/category.html', context=context)


def gamedetail(request, category_name_slug, game_name_slug):
    context = {}

    try:
        game = Games.objects.get(slug=game_name_slug)
        game_category = Category.objects.get(slug=category_name_slug)
        related_games = Games.objects.filter(category=game.category).order_by('?')[:4]
        categories = Category.objects.all
        gamesearch = Games.objects.all()

        context['gamesearch'] = gamesearch
        context['relatedgames'] = related_games
        context['game'] = game
        context['categories'] = categories
        context['game_category'] = game_category

    except Games.DoesNotExist:
        pass

    return render(request, template_name='gamingpatrada/gamedetails.html', context=context)


def review(request):
    context = {}
    categories = Category.objects.all
    gamesearch = Games.objects.all()
    context['gamesearch'] = gamesearch
    context['categories'] = categories
    return render(request, template_name='gamingpatrada/review.html', context=context)


def donate(request):
    context = {}
    categories = Category.objects.all
    gamesearch = Games.objects.all()
    context['gamesearch'] = gamesearch
    context['categories'] = categories
    return render(request, template_name='gamingpatrada/Donate.html', context=context)


def all_games(request):
    context = {}
    categories = Category.objects.all
    context['categories'] = categories
    game = Games.objects.all().order_by('name')
    letters = Letters.objects.all().order_by('letter')
    context['letters'] = letters
    context['allgames'] = game
    return render(request, template_name='gamingpatrada/games.html', context=context)


def gamesort(request, starts_with):
    try:
        context = {}
        letters = Letters.objects.all().order_by('letter')
        context['letters'] = letters
        game = Games.objects.filter(name__istartswith=starts_with)
        context['allgames'] = game
        categories = Category.objects.all
        context['categories'] = categories
    except Games.DoesNotExist:
        pass

    return render(request, template_name='gamingpatrada/gamesort.html', context=context)
