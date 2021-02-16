from ..models.film import Film


def get_all_films():
    return Film.objects.all()
