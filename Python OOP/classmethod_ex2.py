#classmethod example 2

class DateTime:

    def __init__(self, day=10, month=10, year=2000):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, string_date):
        day, month, year = map(int, string_date.split('-'))
        myDate = cls(day, month, year)
        return f"This is my {myDate}."
    
    @staticmethod
    def is_valid_date(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

dateObj = DateTime.from_string('11-08-1994')
is_valid_date = DateTime.is_valid_date('20-05-1994')
print(is_valid_date)
