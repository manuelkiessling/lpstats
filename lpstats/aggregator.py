import datetime
import time

class Aggregator(object):
    def __init__(self, data):
        self.data = data

    def _get_date_of_entry(self, entry_index):
        entry_date_time = time.strptime(self.data[entry_index]['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        return datetime.date(year=entry_date_time.tm_year, month=entry_date_time.tm_mon, day=entry_date_time.tm_mday)

    def get_newest_date(self):
        return self._get_date_of_entry(0)

    def get_oldest_date(self):
        return self._get_date_of_entry(-1)

    def get_date_range(self):
        date_range = []
        oldest_date = self.get_oldest_date()
        diff = self.get_newest_date() - oldest_date
        for i in range(0, diff.days+1):
            date_range.append(oldest_date + datetime.timedelta(days=i))
        return date_range

    def get_number_of_sales_by_day(self):
        sales = {}
        date_range = self.get_date_range()
        for date in date_range:
            sales[date] = 0;
        for index, entry in enumerate(self.data):
            sales[self._get_date_of_entry(index)] += 1
        result = []
        for date in date_range:
            result.append({'date': date, 'number_of_sales': sales[date]})
        return result


New = Aggregator  
