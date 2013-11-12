from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
from lpstats import collector, aggregator, transformer

PORT_NUMBER = 8080

class RequestHandler(BaseHTTPRequestHandler):
    coll = collector.New('<YOUR-LEANPUB-API-KEY-HERE>', '<YOUR-BOOK-SLUG-HERE>')
        #super(RequestHandler, self).__init__()

    def do_GET(self):
        if self.path == '/number_of_sales_by_day.json':
            all_sales = RequestHandler.coll.get_all_sales()
            agg = aggregator.New(all_sales)
            number_of_sales_by_day = agg.get_number_of_sales_by_day()
            tra = transformer.New()
            response = tra.number_of_sales_per_day_to_chartjs_json(number_of_sales_by_day)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response)
            return
        else:
            send_reply = False
            if self.path.endswith('.html'):
                mimetype = 'text/html'
                send_reply = True
            if self.path.endswith('.jpg'):
                mimetype = 'image/jpg'
                send_reply = True
            if self.path.endswith('.gif'):
                mimetype = 'image/gif'
                send_reply = True
            if self.path.endswith('.png'):
                mimetype = 'image/png'
                send_reply = True
            if self.path.endswith('.js'):
                mimetype = 'application/javascript'
                send_reply = True
            if self.path.endswith('.css'):
                mimetype = 'text/css'
                send_reply = True
            
            if send_reply:
                f = open(curdir + sep + 'htdocs' + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

try:
    server = HTTPServer(('', PORT_NUMBER), RequestHandler)
    print 'Started HTTP server on port ', PORT_NUMBER
    server.serve_forever()
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
