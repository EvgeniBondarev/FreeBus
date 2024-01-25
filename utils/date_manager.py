from datetime import datetime, timedelta


def generate_dates():
    current_datetime = datetime.now()

    first_date = current_datetime.now() + timedelta(hours=3)
    second_date = first_date + timedelta(minutes=30)

    formatted_first_date = first_date.strftime('%d.%m.%Y %H:%M')
    formatted_second_date = second_date.strftime('%d.%m.%Y %H:%M')

    return formatted_first_date, formatted_second_date