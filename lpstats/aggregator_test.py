import unittest
import aggregator
import datetime

data = [{'author_paid_out_at':None,
         'author_royalties':3.4,
         'author_royalty_percentage':100.0,
         'cause_paid_out_at':None,
         'cause_royalties':0.0,
         'cause_royalty_percentage':0.0,
         'created_at':'2013-11-12T09:47:47Z',
         'publisher_paid_out_at':None,
         'publisher_royalties':0.0,
         'royalty_days_hold':0,
         'author_username':'manuelkiessling',
         'publisher_slug':'',
         'user_email':'nhisyam3003@gmail.com',
         'purchase_uuid':'1bQcxTtbPAUewpcs3Gm_BB'
        },
        {'author_paid_out_at':None,
         'author_royalties':3.4,
         'author_royalty_percentage':100.0,
         'cause_paid_out_at':None,
         'cause_royalties':0.0,
         'cause_royalty_percentage':0.0,
         'created_at':'2013-11-09T09:47:47Z',
         'publisher_paid_out_at':None,
         'publisher_royalties':0.0,
         'royalty_days_hold':0,
         'author_username':'manuelkiessling',
         'publisher_slug':'',
         'user_email':'nhisyam3003@gmail.com',
         'purchase_uuid':'1bQcxTtbPAUewpcs3Gm_AA'
        },
       ]

class AggregatorTest(unittest.TestCase):
    def test_get_newest_date(self):
        agg = aggregator.New(data)
        newest_date = agg.get_newest_date()

        expected_date = datetime.date(year=2013, month=11, day=12)
        self.assertEquals(expected_date, newest_date)

    def test_get_oldest_date(self):
        agg = aggregator.New(data)
        oldest_date = agg.get_oldest_date()

        expected_date = datetime.date(year=2013, month=11, day=9)
        self.assertEquals(expected_date, oldest_date)

    def test_get_date_range(self):
        agg = aggregator.New(data)
        date_range = agg.get_date_range()

        expected_date_range = [datetime.date(year=2013, month=11, day=9),
                               datetime.date(year=2013, month=11, day=10),
                               datetime.date(year=2013, month=11, day=11),
                               datetime.date(year=2013, month=11, day=12),
                              ]
        self.assertEquals(expected_date_range, date_range)

    def test_get_number_of_sales_by_day(self):
        pass
        agg = aggregator.New(data)
        sales = agg.get_number_of_sales_by_day()

        expected_sales = [{'date':datetime.date(year=2013, month=11, day=9),
                           'number_of_sales':1,
                          },
                          {'date':datetime.date(year=2013, month=11, day=10),
                           'number_of_sales':0,
                          },
                          {'date':datetime.date(year=2013, month=11, day=11),
                           'number_of_sales':0,
                          },
                          {'date':datetime.date(year=2013, month=11, day=12),
                           'number_of_sales':1,
                          },
                         ]
        self.assertEquals(expected_sales, sales)

if __name__ == '__main__':
    unittest.main()
