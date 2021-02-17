from kino.models.pages import HomePage
from django.core.exceptions import ObjectDoesNotExist


def get_home_page() -> HomePage or None:
    try:
        home_page = HomePage.objects.get(id=0)
    except HomePage.DoesNotExist:
        home_page = None
    return home_page
