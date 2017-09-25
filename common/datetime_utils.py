import datetime


class DateTimeUtils:

    @staticmethod
    def date_to_string(date):
        return date.strftime('%Y-%m-%d')

    @staticmethod
    def date_from_string(date_string):
        return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()

    @staticmethod
    def today():
        return datetime.date.today()

    @staticmethod
    def bygone_day(duration, start=None):
        today = start if start is not None else DateTimeUtils.today()
        return today - datetime.timedelta(days=duration)

    @staticmethod
    def start_end_date(duration, start=None):
        today = start if start is not None else DateTimeUtils.today()
        str_today = DateTimeUtils.date_to_string(today)
        bygone_days = DateTimeUtils.bygone_day(duration, today)
        str_bygone_days = DateTimeUtils.date_to_string(bygone_days)
        return str_bygone_days, str_today

if __name__ == '__main__':
    pass
