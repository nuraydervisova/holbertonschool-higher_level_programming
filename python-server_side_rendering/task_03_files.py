from flask import Flask, render_template, request, redirect
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/products?source=json')


def read_json_file():
    with open('products.json') as f:
        return json.load(f)

def read_csv_file():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source", products=[])

    products_list = read_json_file() if source == 'json' else read_csv_file()

    if product_id:
        products_list = [p for p in products_list if p['id'] == product_id]
        if not products_list:
            return render_template('product_display.html', error="Product not found", products=[])

    return render_template('product_display.html', products=products_list, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
