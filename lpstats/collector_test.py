import unittest
import collector

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

class CollectorTest(unittest.TestCase):
    def test_get_all_sales(self):
        coll = collector.New()
        coll.set_api_key('thekey')
        coll.set_book_slug('nodebeginner')
        coll.client.httpclient.request = mock_request_individual_purchases

        all_sales = coll.get_all_sales()
        self.assertEquals(all_sales[3]['author_royalties'], 5.6)

if __name__ == '__main__':
    unittest.main()
