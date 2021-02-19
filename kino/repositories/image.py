from kino.models.image import FilmImage
from kino.models.film import Film


def get_film_image_list_by_id(film_id):
    try:
        film_image_list = FilmImage.objects.filter(film=film_id)
    except Film.DoesNotExist:
        film_image_list = None
    return film_image_list
