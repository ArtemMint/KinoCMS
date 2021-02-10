from django.views.generic import ListView
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404

from kino.models.film import Film
from kino.models.pages import HomePage


def homePageView(request):
    films = Film.objects.all()
    home_page = HomePage.objects.get(id=0)

    context = {"films": films, "home_page": home_page}
    template_name = 'kino/home.html'
    return render(request, template_name, context)