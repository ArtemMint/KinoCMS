from kino.models.film import Film


def get_all_films():
    return Film.objects.all()


def get_film_by_id(film_id) -> Film or None:
    try:
        film = Film.objects.get(id=film_id)
    except Film.DoesNotExist:
        film = None

    return film
