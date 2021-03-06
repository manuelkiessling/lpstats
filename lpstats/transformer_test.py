import unittest
import datetime
import transformer

number_of_sales_per_day = [{'date':datetime.date(year=2013, month=11, day=9),
                           'number_of_sales':19,
                           },
                           {'date':datetime.date(year=2013, month=11, day=10),
                            'number_of_sales':25,
                           },
                          ]

date_range = [datetime.date(year=2013, month=11, day=9),
              datetime.date(year=2013, month=11, day=10),
              datetime.date(year=2013, month=11, day=11)
             ]

class TransformerTest(unittest.TestCase):
    def test_number_of_sales_per_day_to_chartjs_json(self):
        t = transformer.New()
        chartjs_json = t.number_of_sales_per_day_to_chartjs_json(number_of_sales_per_day)

        expected_chartjs_json = '{"labels": ["2013-11-09", "2013-11-10"], "data": [19, 25]}'
        self.assertEquals(expected_chartjs_json, chartjs_json)

    def test_date_range_to_json(self):
        t = transformer.New()
        date_range_json = t.date_range_to_json(date_range)

        expected_date_range_json = '["2013-11-09", "2013-11-10", "2013-11-11"]'
        self.assertEquals(expected_date_range_json, date_range_json)

if __name__ == '__main__':
    unittest.main()
