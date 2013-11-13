from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import urlparse
import time
import datetime
from lpstats import collector, aggregator, transformer

PORT_NUMBER = 8080

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        urlparts = urlparse.urlparse(self.path)
        path = urlparts.path

        if path == '/':
            path = '/index.html'

        if path == '/date_range.json':
            query = urlparse.parse_qs(urlparts.query)
            api_key = query['api_key'][0]
            book_slug = query['book_slug'][0]
            coll.set_api_key(api_key)
            coll.set_book_slug(book_slug)
            all_sales = coll.get_all_sales()
            agg = aggregator.New(all_sales)
            date_range = agg.get_date_range()
            tra = transformer.New()
            response = tra.date_range_to_json(date_range)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response)
            return

        if path == '/number_of_sales_by_day.json':
            query = urlparse.parse_qs(urlparts.query)
            api_key = query['api_key'][0]
            book_slug = query['book_slug'][0]
            start_date = query['start_date'][0]
            end_date = query['end_date'][0]
            if start_date == 'null' or end_date == 'null':
                start_date = None
                end_date = None
            else:
                start_date = time.strptime(start_date, '%Y-%m-%d')
                end_date = time.strptime(end_date, '%Y-%m-%d')
                start_date = datetime.date(year=start_date.tm_year, month=start_date.tm_mon, day=start_date.tm_mday)
                end_date = datetime.date(year=end_date.tm_year, month=end_date.tm_mon, day=end_date.tm_mday)
            coll.set_api_key(api_key)
            coll.set_book_slug(book_slug)
            all_sales = coll.get_all_sales()
            agg = aggregator.New(all_sales)
            number_of_sales_by_day = agg.get_number_of_sales_by_day(start_date=start_date, end_date=end_date)
            tra = transformer.New()
            response = tra.number_of_sales_per_day_to_chartjs_json(number_of_sales_by_day)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response)
            return

        else:
            send_reply = False
            if path.endswith('.html'):
                mimetype = 'text/html'
                send_reply = True
            if path.endswith('.jpg'):
                mimetype = 'image/jpg'
                send_reply = True
            if path.endswith('.gif'):
                mimetype = 'image/gif'
                send_reply = True
            if path.endswith('.png'):
                mimetype = 'image/png'
                send_reply = True
            if path.endswith('.js'):
                mimetype = 'application/javascript'
                send_reply = True
            if path.endswith('.css'):
                mimetype = 'text/css'
                send_reply = True
            
            if send_reply:
                f = open(curdir + sep + 'htdocs' + path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('404 Not found')
            return

def mock_request_individual_purchases(url):
    if url == 'https://leanpub.com/test/individual_purchases.json?api_key=123&page=1':
        resp = {}
        content = '[{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-18T09:47:47Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"nhisyam3003@gmail.com","purchase_uuid":"1bQcxTtbPAUewpcs3Gm_BQ"},{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-13T09:47:47Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"nhisyam3003@gmail.com","purchase_uuid":"1bQcxTtbPAUewpcs3Gm_BQ"},{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T09:47:47Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"nhisyam3003@gmail.com","purchase_uuid":"1bQcxTtbPAUewpcs3Gm_BQ"},{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T09:12:24Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"sgnt710@yahoo.com","purchase_uuid":"3c-TnWjIf9hPIErs9Yfh6s"},{"author_paid_out_at":null,"author_royalties":"3.4","author_royalty_percentage":"100.0","cause_paid_out_at":null,"cause_royalties":"0.0","cause_royalty_percentage":"0.0","created_at":"2013-11-12T07:43:20Z","publisher_paid_out_at":null,"publisher_royalties":"0.0","royalty_days_hold":0,"author_username":"manuelkiessling","publisher_slug":"","user_email":"","purchase_uuid":"0KD3jJ8K9EmQ63O4q1sZ9g"}]'
        return (resp, content)
    else:
        return ({}, '[]')

if __name__ == '__main__':
    try:
        coll = collector.New()
        #coll.client.httpclient.request = mock_request_individual_purchases
        server = HTTPServer(('', PORT_NUMBER), RequestHandler)
        print 'Started HTTP server on port', PORT_NUMBER
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
