import client

class Collector(object):
    def __init__(self):
        self.client = client.New()

    def set_api_key(self, api_key):
        self.client.set_api_key(api_key)

    def set_book_slug(self, book_slug):
        self.client.set_book_slug(book_slug)

    def get_all_sales(self):
        end_reached = False
        all_sales = []
        page = 1
        while not end_reached:
            individual_purchases = self.client.get_individual_purchases(page)
            if len(individual_purchases):
                all_sales.extend(individual_purchases)
            else:
                end_reached = True
            page += 1
        return all_sales

New = Collector
