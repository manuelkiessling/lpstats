import unittest
import client

def mock_request_sales_summary(url):
    if url != 'https://leanpub.com/nodebeginner/sales.json?api_key=thekey':
        raise Exception
    resp = {}
    content = '{"book":"nodebeginner","url":"https://leanpub.com/nodebeginner","total_author_royalties":"100.00","total_book_royalties":"200.00","num_happy_readers":9639,"num_happy_paid_purchases":9408,"num_refunded_purchases":49,"unpaid_royalties":"50.00","royalties_currently_due":"0.0","royalties_due_on_first_of_next_month":"75.00","paid_royalties":"500.00"}'
    return (resp, content)

def mock_request_individual_purchases(url):
    if url == 'https://leanpub.com/nodebeginner/individual_purchases.json?api_key=thekey&page=1':
        resp = {}
        content = '[{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T09:47:47Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"nhisyam3003@gmail.com","purchase_uuid":"1bQcxTtbPAUewpcs3Gm_BQ"},{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T09:12:24Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"sgnt710@yahoo.com","purchase_uuid":"3c-TnWjIf9hPIErs9Yfh6s"},{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T07:43:20Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"","purchase_uuid":"0KD3jJ8K9EmQ63O4q1sZ9g"}]'
        return (resp, content)
    if url == 'https://leanpub.com/nodebeginner/individual_purchases.json?api_key=thekey&page=2':
        resp = {}
        content = '[{"author_paid_out_at":null,"author_royalties":"5.6","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T09:47:47Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"nhisyam3003@gmail.com","purchase_uuid":"1bQcxTtbPAUewpcs3Gm_BQ"},{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T09:12:24Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"sgnt710@yahoo.com","purchase_uuid":"3c-TnWjIf9hPIErs9Yfh6s"},{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T07:43:20Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"","purchase_uuid":"0KD3jJ8K9EmQ63O4q1sZ9g"}]'
        return (resp, content)
    if url == 'https://leanpub.com/nodebeginner/individual_purchases.json?api_key=thekey&page=3':
        resp = {}
        content = '[]'
        return (resp, content)
    raise Exception

def mock_request_individual_purchases_after_cache(url):
    if url == 'https://leanpub.com/nodebeginner/individual_purchases.json?api_key=thekey&page=1':
        resp = {}
        content = '[{"author_paid_out_at":null,"author_royalties":"7.7","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T09:47:47Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"nhisyam3003@gmail.com","purchase_uuid":"1bQcxTtbPAUewpcs3Gm_BQ"},{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T09:12:24Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"sgnt710@yahoo.com","purchase_uuid":"3c-TnWjIf9hPIErs9Yfh6s"},{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T07:43:20Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"","purchase_uuid":"0KD3jJ8K9EmQ63O4q1sZ9g"}]'
        return (resp, content)
    raise Exception

class ClientTest(unittest.TestCase):
    def test_sales_summary(self):
        c = client.New()
        c.httpclient.request = mock_request_sales_summary
        c.set_api_key('thekey')
        c.set_book_slug('nodebeginner')

        sales_summary = c.get_sales_summary()
        self.assertEquals(sales_summary['total_author_royalties'], 100.0)
        self.assertEquals(sales_summary['book'], 'nodebeginner')

    def test_get_individual_purchases(self):
        c = client.New()
        c.httpclient.request = mock_request_individual_purchases
        c.set_api_key('thekey')
        c.set_book_slug('nodebeginner')

        individual_purchases = c.get_individual_purchases()
        self.assertEquals(individual_purchases[0]['author_royalties'], 3.4)

        individual_purchases = c.get_individual_purchases(page=2)
        self.assertEquals(individual_purchases[0]['author_royalties'], 5.6)

        individual_purchases = c.get_individual_purchases(page=3)
        self.assertEquals(individual_purchases, [])

    def test_get_individual_purchases_cache(self):
        c = client.New()
        c.httpclient.request = mock_request_individual_purchases
        c.set_api_key('thekey')
        c.set_book_slug('nodebeginner')

        individual_purchases = c.get_individual_purchases()
        self.assertEquals(individual_purchases[0]['author_royalties'], 3.4)

        c.httpclient.request = mock_request_individual_purchases_after_cache
        individual_purchases = c.get_individual_purchases()
        self.assertEquals(individual_purchases[0]['author_royalties'], 3.4)
