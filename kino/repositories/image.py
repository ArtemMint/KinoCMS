from ..models.image import FilmImage
from ..models.film import Film


def get_film_image_list_by_id(film_id):
    try:
        film_image_list = FilmImage.objects.filter(film=film_id)
    except Film.DoesNotExist:
        film_image_list = None
    print([image.image.url for image in film_image_list])
    return film_image_list
