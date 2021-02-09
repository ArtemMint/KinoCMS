from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from kino.models.pages import HomePage
from kino.forms.pages import HomepageForm


def adminPagesView(request):
    pages = HomePage.objects.all()

    context = {'pages': pages}
    return render(request, 'admin_panel/pages.html', context)

def adminHomePageView(request):
    try:
        homepage = HomePage.objects.get(id=0)
    except homepage.DoesNotExist:
        HomePage.objects.create(id=0,seo_title='',seo_keywords='',seo_description='',phone1='',phone2='')
        homepage = get_object_or_404(HomePage, id=0)

    if request.method == "POST":
        form = HomepageForm(request.POST, instance=homepage)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = HomepageForm(instance=homepage)

    context = {'home_form': form}

    return render(request, 'admin_panel/home_page.html', context)
