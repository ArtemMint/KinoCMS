from ..repositories.users import get_all_users_email_list
from django.core.mail import send_mail, send_mass_mail, mail_admins
from ..forms.mailing import MalingForm
from kinocms.settings import EMAIL_HOST_USER


def mail_users(request, to_email_list: list) -> None:
    form = MalingForm(request.POST or None)
    if form.is_valid():
        send_mail(subject=request.subject,
                  message=request.message,
                  from_email=EMAIL_HOST_USER,
                  recipient_list=to_email_list)

