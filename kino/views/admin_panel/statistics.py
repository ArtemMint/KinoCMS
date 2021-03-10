from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')
from utils import get_avg_age

from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, \
    get_object_or_404, get_list_or_404

from kino.models.shares import Shares
from kino.models.news import News
from kino.models.film import Film
from kino.models.cinema import Cinema, CinemaHall
from register.models.client import Client
from ...repositories.shares import *
from ...repositories.news import *
from ...repositories.cinema import *
from ...repositories.film import *
from ...repositories.users import *
from kino.charts.charts import *


@permission_required('is_staff')
def adminStatisticsView(request):
    """
    Statistics page which contains all main information about DB
    """
    get_bar_chart()
    get_pie_chart()
    return render(
        request,
        'admin_panel/statistics.html',
        {
            'users': get_users_count(),
            'men': get_men_count(),
            'women': get_women_count(),
            'avg_age': get_users_avg_age(),
            'men_avg_age': get_men_avg_age(),
            'women_avg_age': get_women_avg_age(),
            'films': get_films_count(),
            'cinemas': get_cinema_count(),
            'num_news': get_news_count(),
            'num_shares': get_shares_count(),
        }
    )
