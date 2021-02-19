from django.shortcuts import redirect, render

from ...repositories.pages import get_home_page



def schedule_page_view(request):
    return render(
        request, 'kino/schedule.html',
        {
            'home_page': get_home_page(),
        }
    )
