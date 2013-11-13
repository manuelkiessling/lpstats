import httplib2
import json

class Client(object):
    def __init__(self):
        self._cache = {'individual_purchases_page':{}}
        self.httpclient = httplib2.Http(".cache", disable_ssl_certificate_validation=True)

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_book_slug(self, book_slug):
        self.book_slug = book_slug

    def get_sales_summary(self):
        resp, content = self.httpclient.request('https://leanpub.com/' + str(self.book_slug) + '/sales.json?api_key=' + str(self.api_key))
        raw_sales_summary = json.loads(content)
        sales_summary = {}
        for key, val in raw_sales_summary.iteritems():
            if val:
                try:
                    val = float(val)
                except ValueError:
                    pass
            sales_summary[key] = val
        return sales_summary

    def get_individual_purchases(self, page=1):
        cacheid = self.book_slug + self.api_key + str(page)
        if self._cache['individual_purchases_page'].get(cacheid) != None:
            return self._cache['individual_purchases_page'][cacheid]
        resp, content = self.httpclient.request('https://leanpub.com/' + str(self.book_slug) + '/individual_purchases.json?api_key=' + str(self.api_key) + '&page=' + str(page))
        raw_individual_purchases = json.loads(content)
        individual_purchases = []
        for raw_individual_purchase in raw_individual_purchases:
            individual_purchase = {}
            for key, val in raw_individual_purchase.iteritems():
                if val:
                    try:
                        val = float(val)
                    except ValueError:
                        pass
                individual_purchase[key] = val
            individual_purchases.append(individual_purchase)
        self._cache['individual_purchases_page'][cacheid] = individual_purchases
        return individual_purchases

New = Client
