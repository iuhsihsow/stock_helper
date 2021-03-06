import datetime


class DateTimeUtils:

    @staticmethod
    def stock_today():
        if int(datetime.datetime.now().time().strftime('%H')) > 20:
            return DateTimeUtils.today()
        else:
            return DateTimeUtils.bygone_day(1)

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
    def bygone_day(duration, end=None):
        today = end if end is not None else DateTimeUtils.today()
        return today - datetime.timedelta(days=duration)

    @staticmethod
    def start_end_date(duration, end=None):
        today = end if end is not None else DateTimeUtils.today()
        str_today = DateTimeUtils.date_to_string(today)
        bygone_days = DateTimeUtils.bygone_day(duration, today)
        str_bygone_days = DateTimeUtils.date_to_string(bygone_days)
        return str_bygone_days, str_today

if __name__ == '__main__':
    pass
