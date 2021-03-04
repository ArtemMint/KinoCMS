"""Image requests to DB
"""

from ..models.image import FilmImage
from ..models.film import Film


def get_film_image_list_by_id(film_id):
    """Get film images by film_id

    Args:
        film_id (int): film_id

    Returns:
        queryset: set of images by film
    """
    try:
        film_image_list = FilmImage.objects.filter(film=film_id)
    except Film.DoesNotExist:
        film_image_list = None
        print(film_image_list)
    return film_image_list

def get_images_ids(film):
    """get ids images

    Args:
        film (int): film id

    Returns:
        queryset: queryset with images
    """
    images_ids = FilmImage.objects.values_list().filter(film=film)
    print(images_ids)
    return images_ids
