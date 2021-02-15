from django.shortcuts import redirect, render, get_object_or_404
from kino.models.film import Film
from kino.models.pages import HomePage


def homePageView(request):
    films = Film.objects.order_by('-id')
    home_page = get_object_or_404(HomePage)

    context = {"films": films, "home_page": home_page}
    template_name = 'kino/home.html'
    return render(request, template_name, context)
