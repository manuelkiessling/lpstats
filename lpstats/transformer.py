import json

class Transformer(object):
    def number_of_sales_per_day_to_chartjs_json(self, number_of_sales_per_day):
        labels = [str(entry['date']) for entry in number_of_sales_per_day]
        data = [entry['number_of_sales'] for entry in number_of_sales_per_day]
        return json.dumps({'labels': labels, 'data': data})

New = Transformer
