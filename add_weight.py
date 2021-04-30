import persistance
import datetime


def string_to_date(date):
    if date is None:
        return datetime.datetime.utcnow()
    else:
        return datetime.datetime.strptime(date, '%d/%m/%y %H:%M:%S')


def weight_adder(weight, date):

    mongo_date = string_to_date(date)

    persistance.insert({
        "weight": round(weight, 1),
        "date-stamp": mongo_date
    })