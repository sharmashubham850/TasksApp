from datetime import datetime


def date_to_str(string):
    date_object = datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')
    return datetime.strftime(date_object, '%d %b %Y')
