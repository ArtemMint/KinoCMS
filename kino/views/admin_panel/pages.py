from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from kino.models.pages import HomePage, Contacts, Page
from kino.forms.pages import HomepageForm, ContactsForm, PageForm


def adminPagesView(request):
    pages = HomePage.objects.all()

    context = {'pages': pages}
    return render(request, 'admin_panel/pages.html', context)


def adminHomePageView(request):
    try:
        homepage = HomePage.objects.get(id=0)
<<<<<<< HEAD
    except ObjectDoesNotExist:
=======
    except HomePage.DoesNotExist:
        homepage = None
>>>>>>> ceb387be7751357c92d286947222bfe1b4e62b3a
        HomePage.objects.create(
            id=0, seo_title='', seo_keywords='', seo_description='', phone1='', phone2='')
        homepage = get_object_or_404(HomePage, id=0)

    form = HomepageForm(request.POST or None, instance=homepage or None)

    if request.method == "POST":
        form = HomepageForm(request.POST, instance=homepage)
        if form.is_valid():
            form.save()
            return redirect('admin_users')

    context = {'form': form}

    return render(request, 'admin_panel/pages/home_page.html', context)


def adminContactsPageView(request):
    try:
        contacts = Contacts.objects.get(id=0)
    except ObjectDoesNotExist:
        Contacts.objects.create(id=0, seo_title='', seo_keywords='',
                                seo_description='', name='', address='', status=False, coordinates='0')
        contacts = get_object_or_404(Contacts, id=0)

    if request.method == "POST":
        form = ContactsForm(request.POST, request.FILES, instance=contacts)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = ContactsForm(instance=contacts)

    context = {'form': form}
    template_name = 'admin_panel/pages/contacts_page.html'
    return render(request, template_name, context)


def adminAboutPageView(request):
    try:
        about = Page.objects.get(id=0)
    except ObjectDoesNotExist:
        Page.objects.create(id=0, seo_title='', seo_keywords='', seo_description='', name='', description='',
                            status=False, preview='', image1='', image2='', image3='', image4='', image5='')
        about = get_object_or_404(Page, id=0)

    if request.method == "POST":
        form = PageForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = PageForm(instance=about)

    context = {'form': form}
    template_name = 'admin_panel/pages/about_page.html'
    return render(request, template_name, context)


def adminCafeBarPageView(request):
    try:
        cafe = Page.objects.get(id=1)
    except ObjectDoesNotExist:
        Page.objects.create(id=1, seo_title='', seo_keywords='', seo_description='', name='', description='',
                            status=False, preview='', image1='', image2='', image3='', image4='', image5='')
        cafe = get_object_or_404(Page, id=1)

    if request.method == "POST":
        form = PageForm(request.POST, request.FILES, instance=cafe)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = PageForm(instance=cafe)

    context = {'form': form}
    template_name = 'admin_panel/pages/cafe_bar.html'
    return render(request, template_name, context)


def adminVipHallPageView(request):
    try:
        viphall = Page.objects.get(id=2)
    except ObjectDoesNotExist:
        Page.objects.create(id=2, seo_title='', seo_keywords='', seo_description='', name='', description='',
                            status=False, preview='', image1='', image2='', image3='', image4='', image5='')
        viphall = get_object_or_404(Page, id=2)

    if request.method == "POST":
        form = PageForm(request.POST, request.FILES, instance=viphall)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = PageForm(instance=viphall)

    context = {'form': form}
    template_name = 'admin_panel/pages/vip_hall.html'
    return render(request, template_name, context)


def adminAdvertisingPageView(request):
    try:
        advertising = Page.objects.get(id=3)
    except ObjectDoesNotExist:
        Page.objects.create(id=3, seo_title='', seo_keywords='', seo_description='', name='', description='',
                            status=False, preview='', image1='', image2='', image3='', image4='', image5='')
        advertising = get_object_or_404(Page, id=3)

    if request.method == "POST":
        form = PageForm(request.POST, request.FILES, instance=advertising)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = PageForm(instance=advertising)

    context = {'form': form}
    template_name = 'admin_panel/pages/advertising.html'
    return render(request, template_name, context)


def adminChildrenRoomPageView(request):
    try:
        children = Page.objects.get(id=4)
    except ObjectDoesNotExist:
        Page.objects.create(id=4, seo_title='', seo_keywords='', seo_description='', name='', description='',
                            status=False, preview='', image1='', image2='', image3='', image4='', image5='')
        children = get_object_or_404(Page, id=4)

    if request.method == "POST":
        form = PageForm(request.POST, request.FILES, instance=children)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = PageForm(instance=children)

    context = {'form': form}
    template_name = 'admin_panel/pages/children_room.html'
    return render(request, template_name, context)
