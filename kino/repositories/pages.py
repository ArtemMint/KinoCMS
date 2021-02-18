from kino.models.pages import HomePage
from kino.models.pages import Page
from kino.models.image import ChildrenRoomImage
from django.core.exceptions import ObjectDoesNotExist


def get_home_page() -> HomePage or None:
    try:
        home_page = HomePage.objects.get(id=0)
    except HomePage.DoesNotExist:
        home_page = None
    return home_page


def get_children_room_page() -> HomePage or None:
    try:
        children_room = Page.objects.get(id=4)
    except HomePage.DoesNotExist:
        children_room = None
    return children_room

def get_children_room_image_list_by_id(children_room):
    try:
        children_room_image_list = ChildrenRoomImage.objects.filter(children_room=children_room)
    except ChildrenRoomImage.DoesNotExist:
        children_room_image_list = None
    return children_room_image_list