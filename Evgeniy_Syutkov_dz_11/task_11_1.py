class OwnError(Exception):
    pass


class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def int_date(cls, str_date):
        day, month, year = str_date.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def validator(date):
        try:
            day, month, year = date.split('-')
            if (int(day) < 1 or int(day) > 31) or (int(month) < 1 or int(month) > 12):
                raise OwnError('Неправильная дата')
            return date
        except OwnError as err:
            return err


print(Date.int_date('03-12-2020'))
print(Date.validator('00-12-2020'))
