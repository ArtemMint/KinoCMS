import datetime


def current_year():
    return datetime.datetime.now().year

def get_avg_age(set_of_users):
    avg_age = 0
    for user in set_of_users:
        if user.birth_date == None:
            pass
        else:
            avg_age = avg_age + user.get_age()

    return avg_age // set_of_users.count()  
