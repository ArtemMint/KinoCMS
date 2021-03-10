from kino.models.film import Film


def get_all_films():
    """get all films

    Returns:
        queryset: film
    """
    return Film.objects.all()


def get_films_count():
    return get_all_films().count()


def get_film_by_id(film_id):
    """get one film by id

    Args:
        film_id (int): film_id

    Returns:
        queryset: film
    """
    try:
        film = Film.objects.get(id=film_id)
    except Film.DoesNotExist:
        film = None

    return film
