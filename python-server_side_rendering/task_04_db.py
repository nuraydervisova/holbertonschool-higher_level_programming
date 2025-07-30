from flask import Flask, render_template, request, redirect
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    # Əsas səhifədən /products?source=json-ə yönləndirir
    return redirect('/products?source=json')

def get_data_from_json():
    with open('products.json') as f:
        return json.load(f)

def get_data_from_csv():
    data = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def get_data_from_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        return products
    except Exception as e:
        return {"error": str(e)}

@app.route('/products')
def products():
    source = request.args.get('source')

    if source == 'json':
        products = get_data_from_json()
    elif source == 'csv':
        products = get_data_from_csv()
    elif source == 'sql':
        result = get_data_from_sqlite()
        if isinstance(result, dict) and "error" in result:
            return f"Database error: {result['error']}"
        products = result
    else:
        return "Wrong source"

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True)
