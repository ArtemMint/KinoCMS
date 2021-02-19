from django.shortcuts import render, redirect, \
    get_object_or_404, get_list_or_404
from django.contrib.auth.models import User

from register.models.client import Client
from kino.models.cinema import Cinema, CinemaHall
from kino.models.film import Film
from kino.models.news import News
from utils import get_avg_age


def adminStatisticsView(request):
    """
    Statistics page which contains all main information about DB
    """
    all = Client.objects.all()
    men = Client.objects.filter(gender='Male')
    women = Client.objects.filter(gender='Female')

    num_users = all.count()
    num_men = men.count()
    num_women = women.count()

    # Average age of Users
    avg_age = get_avg_age(all)
    men_avg_age = get_avg_age(men)
    women_avg_age = get_avg_age(women)

    num_films = Film.objects.count()
    num_cinemas = Cinema.objects.count()
    num_news = News.objects.count()

    context = {'users': num_users, 'men': num_men, 'women': num_women,
               'avg_age': avg_age, 'men_avg_age': men_avg_age, 'women_avg_age': women_avg_age,
               'films': num_films, 'cinemas': num_cinemas, 'num_news': num_news}

    return render(request, 'admin_panel/statistics.html', context)
