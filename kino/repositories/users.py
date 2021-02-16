from django.contrib.auth.models import User


def get_all_users_email_list() -> list:
    email_list = [user.email for user in User.objects.all()]
    return email_list
