
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, \
    get_list_or_404, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import permission_required

from kino.models.pages import HomePage, Contacts, Page
from kino.models.image import *
from kino.forms.pages import *
from kino.repositories.pages import *


@permission_required('is_staff')
def admin_pages_view(request):
    return render(
        request,
        'admin_panel/pages.html',
        {'pages': get_home_page()}
    )


@permission_required('is_staff')
def admin_home_page_view(request):

    form = HomepageForm(
        request.POST or None,
        instance=get_home_page() or None)

    if request.method == "POST":
        form = HomepageForm(
            request.POST,
            instance=get_home_page()
        )
        if form.is_valid():
            form.save()
            return redirect('admin_statistics')

    return render(
        request,
        'admin_panel/pages/home_page.html',
        {'form': form}
    )


@permission_required('is_staff')
def admin_contacts_page_view(request):

    if request.method == "POST":
        form = ContactsForm(
            request.POST,
            request.FILES,
            instance=get_contacts_page()
        )
        if form.is_valid():
            form.save()
            return redirect('admin_statistics')
    else:
        form = ContactsForm(
            instance=get_contacts_page()
        )

    return render(
        request,
        'admin_panel/pages/contacts_page.html',
        {'form': form}
    )


@permission_required('is_staff')
def admin_cafe_bar_page_view(request):
    PageFormSet = inlineformset_factory(
        Page,
        CafeBarImage,
        fields='__all__',
        extra=5,
        max_num=5,
    )

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES,
            instance=get_cafe_bar_page()
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=get_cafe_bar_page()
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=get_cafe_bar_page())
        formset = PageFormSet(instance=get_cafe_bar_page())

    return render(
        request,
        'admin_panel/pages/cafe_bar.html',
        {
            'form': form,
            'formset': formset
        }
    )


@permission_required('is_staff')
def admin_vip_hall_page_view(request):
    PageFormSet = inlineformset_factory(
        Page,
        VipHallImage,
        fields='__all__',
        extra=5,
        max_num=5,
    )

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES,
            instance=get_vip_hall_page()
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=get_vip_hall_page()
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=get_vip_hall_page())
        formset = PageFormSet(instance=get_vip_hall_page())

    return render(
        request,
        'admin_panel/pages/vip_hall.html',
        {
            'form': form,
            'formset': formset
        }
    )


@permission_required('is_staff')
def admin_advertising_page_view(request):
    PageFormSet = inlineformset_factory(
        Page,
        AdvertisingImage,
        fields='__all__',
        extra=5,
        max_num=5,
    )

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES,
            instance=get_advertising_page()
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=get_advertising_page()
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=get_advertising_page())
        formset = PageFormSet(instance=get_advertising_page())

    return render(
        request,
        'admin_panel/pages/advertising.html',
        {
            'form': form,
            'formset': formset
        }
    )


@permission_required('is_staff')
def admin_children_room_page_view(request):
    PageFormSet = inlineformset_factory(
        Page,
        ChildrenRoomImage,
        fields='__all__',
        extra=5,
        max_num=5,
    )

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES,
            instance=get_children_room_page()
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=get_children_room_page()
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=get_children_room_page())
        formset = PageFormSet(instance=get_children_room_page())

    return render(
        request,
        'admin_panel/pages/children_room.html',
        {
            'form': form,
            'formset': formset
        }
    )


@permission_required('is_staff')
def admin_mobile_app_page_view(request):
    PageFormSet = inlineformset_factory(
        Page,
        MobileAppImage,
        fields='__all__',
        extra=5,
        max_num=5,
    )

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES,
            instance=get_mobile_app_page()
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=get_mobile_app_page()
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=get_mobile_app_page())
        formset = PageFormSet(instance=get_mobile_app_page())

    return render(
        request,
        'admin_panel/pages/mobile_app.html',
        {
            'form': form,
            'formset': formset
        }
    )
