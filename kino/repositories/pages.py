from kino.models.pages import HomePage
from kino.models.pages import Page
from kino.models.pages import Contacts
from kino.models.image import *
from django.core.exceptions import ObjectDoesNotExist


def get_home_page() -> HomePage or None:
    try:
        home_page = HomePage.objects.get(id=0)
    except HomePage.DoesNotExist:
        home_page = None
    return home_page


def get_cafe_bar_page() -> HomePage or None:
    try:
        cafe_bar = Page.objects.get(id=1)
    except HomePage.DoesNotExist:
        cafe_bar = None
    return cafe_bar


def get_cafe_bar_image_list_by_id(cafe_bar):
    try:
        cafe_bar_image_list = CafeBarImage.objects.filter(cafe_bar=cafe_bar)
    except CafeBarImage.DoesNotExist:
        cafe_bar_image_list = None
    return cafe_bar_image_list


def get_vip_hall_page() -> HomePage or None:
    try:
        vip_hall = Page.objects.get(id=2)
    except HomePage.DoesNotExist:
        vip_hall = None
    return vip_hall


def get_vip_hall_image_list_by_id(vip_hall):
    try:
        vip_hall_image_list = VipHallImage.objects.filter(vip_hall=vip_hall)
    except VipHallImage.DoesNotExist:
        vip_hall_image_list = None
    return vip_hall_image_list


def get_advertising_page() -> HomePage or None:
    try:
        advertising = Page.objects.get(id=3)
    except HomePage.DoesNotExist:
        advertising = None
    return advertising


def get_advertising_image_list_by_id(advertising):
    try:
        advertising_image_list = AdvertisingImage.objects.filter(
            advertising=advertising)
    except AdvertisingImage.DoesNotExist:
        advertising_image_list = None
    return advertising_image_list


def get_children_room_page() -> HomePage or None:
    try:
        children_room = Page.objects.get(id=4)
    except HomePage.DoesNotExist:
        children_room = None
    return children_room


def get_children_room_image_list_by_id(children_room):
    try:
        children_room_image_list = ChildrenRoomImage.objects.filter(
            children_room=children_room)
    except ChildrenRoomImage.DoesNotExist:
        children_room_image_list = None
    return children_room_image_list


def get_mobile_app_page() -> HomePage or None:
    try:
        mobile_app = Page.objects.get(id=5)
    except HomePage.DoesNotExist:
        mobile_app = None
    return mobile_app


def get_mobile_app_image_list_by_id(mobile_app):
    try:
        mobile_app_list = MobileAppImage.objects.filter(mobile=mobile_app)
    except AdvertisingImage.DoesNotExist:
        mobile_app_list = None
    return mobile_app_list


def get_contacts_page() -> HomePage or None:
    try:
        contacts = Contacts.objects.get(id=0)
    except Contacts.DoesNotExist:
        contacts = None
    return contacts

