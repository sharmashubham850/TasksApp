from datetime import datetime


def date_to_str(string):
    date_object = datetime.strptime(string, '%Y-%m-%d %I:%M:%S.%f')
    return datetime.strftime(date_object, '%d-%b-%Y %I:%M:%S')
