from django.core.mail import send_mail, send_mass_mail, mail_admins
from kinocms.settings import EMAIL_HOST_USER


def mail_users(form, to_email_list: list) -> None:
    if form.is_valid():
        send_mail(subject=form.cleaned_data['subject'],
                  message=form.cleaned_data['message'],
                  from_email=EMAIL_HOST_USER,
                  recipient_list=to_email_list)
