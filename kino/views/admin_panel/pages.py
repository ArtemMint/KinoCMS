
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, \
    get_list_or_404, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import permission_required

from kino.models.pages import HomePage, Contacts, Page
from kino.models.image import *
from kino.forms.pages import *


@permission_required('is_staff')
def admin_pages_view(request):
    pages = HomePage.objects.all()

    return render(
        request,
        'admin_panel/pages.html',
        {'pages': pages}
    )


@permission_required('is_staff')
def admin_home_page_view(request):
    try:
        homepage = HomePage.objects.get(id=0)
    except ObjectDoesNotExist:
        HomePage.objects.create(
            id=0,
            seo_title='',
            seo_keywords='',
            seo_description='',
            phone1='',
            phone2='',
        )
        homepage = get_object_or_404(HomePage, id=0)

    form = HomepageForm(
        request.POST or None,
        instance=homepage or None)

    if request.method == "POST":
        form = HomepageForm(request.POST, instance=homepage)
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
    try:
        contacts = Contacts.objects.get(id=0)
    except ObjectDoesNotExist:
        Contacts.objects.create(
            id=0,
            seo_title='',
            seo_keywords='',
            seo_description='',
            address='',
            status=False,
            coordinates='0',
        )
        contacts = get_object_or_404(Contacts, id=0)

    if request.method == "POST":
        form = ContactsForm(
            request.POST,
            request.FILES,
            instance=contacts
        )
        if form.is_valid():
            form.save()
            return redirect('admin_statistics')
    else:
        form = ContactsForm(instance=contacts)

    return render(
        request,
        'admin_panel/pages/contacts_page.html',
        {'form': form}
    )


@permission_required('is_staff')
def admin_about_page_view(request):
    PageFormSet = inlineformset_factory(
        Page,
        AboutImage,
        fields='__all__',
        extra=5,
        max_num=5,
    )

    try:
        about = Page.objects.get(id=0)
    except ObjectDoesNotExist:
        Page.objects.create(
            id=0,
            seo_title='',
            seo_keywords='',
            seo_description='',
            name='',
            description='',
            status=False,
            preview='',
        )
        about = get_object_or_404(Page, id=0)

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES,
            instance=about
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=about)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=about)
        formset = PageFormSet(instance=about)

    return render(
        request,
        'admin_panel/pages/about_page.html',
        {'form': form, 'formset': formset}
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
    try:
        cafe = Page.objects.get(id=1)
    except ObjectDoesNotExist:
        Page.objects.create(
            id=1,
            seo_title='',
            seo_keywords='',
            seo_description='',
            name='',
            description='',
            status=False,
            preview='',
        )
        cafe = get_object_or_404(Page, id=1)

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES,
            instance=cafe
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=cafe)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=cafe)
        formset = PageFormSet(instance=cafe)

    return render(
        request,
        'admin_panel/pages/cafe_bar.html',
        {'form': form, 'formset': formset}
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
    try:
        viphall = Page.objects.get(id=2)
    except ObjectDoesNotExist:
        Page.objects.create(
            id=2,
            seo_title='',
            seo_keywords='',
            seo_description='',
            name='',
            description='',
            status=False,
            preview='',
        )
        viphall = get_object_or_404(Page, id=2)

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES
            instance=viphall
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=viphall
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=viphall)
        formset = PageFormSet(instance=viphall)

    return render(
        request,
        'admin_panel/pages/vip_hall.html',
        {'form': form, 'formset': formset}
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
    try:
        advertising = Page.objects.get(id=3)
    except ObjectDoesNotExist:
        Page.objects.create(
            id=3,
            seo_title='',
            seo_keywords='',
            seo_description='',
            name='',
            description='',
            status=False,
            preview='',
        )
        advertising = get_object_or_404(Page, id=3)

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES,
            instance=advertising
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=advertising
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=advertising)
        formset = PageFormSet(instance=advertising)

    return render(
        request,
        'admin_panel/pages/advertising.html',
        {'form': form, 'formset': formset}
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

    try:
        children = Page.objects.get(id=4)
    except ObjectDoesNotExist:
        Page.objects.create(
            id=4,
            seo_title='',
            seo_keywords='',
            seo_description='',
            name='',
            description='',
            status=False,
            preview='',
        )
        children = get_object_or_404(Page, id=4)

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES,
            instance=children
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=children
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=children)
        formset = PageFormSet(instance=children)

    return render(
        request,
        'admin_panel/pages/children_room.html',
        {'form': form, 'formset': formset}
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

    try:
        mobile_app = Page.objects.get(id=5)
    except ObjectDoesNotExist:
        Page.objects.create(
            id=5,
            seo_title='',
            seo_keywords='',
            seo_description='',
            name='',
            description='',
            status=False,
            preview='',
        )
    mobile_app = get_object_or_404(Page, id=5)

    if request.method == "POST":
        form = PageForm(
            request.POST,
            request.FILES,
            instance=mobile_app
        )
        formset = PageFormSet(
            request.POST,
            request.FILES,
            instance=mobile_app
        )
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_statistics')
    else:
        form = PageForm(instance=mobile_app)
        formset = PageFormSet(instance=mobile_app)

    return render(
        request,
        'admin_panel/pages/mobile_app.html',
        {'form': form, 'formset': formset}
    )
