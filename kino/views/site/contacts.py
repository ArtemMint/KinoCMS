from django.shortcuts import redirect, render


from ...repositories.pages import *
from ...repositories.ads import *
from ...repositories.banners import * 
from ...models.cinema import Cinema

def contacts_page_view(request):
    return render(
        request, 'kino/contacts.html',
        {
            'contacts': get_contacts_page(),
            'cinema_list': Cinema.objects.all(),
            'home_page': get_home_page(),
            'ads':get_ads_last(),
            'background': get_back_banner(),
        }
    )
