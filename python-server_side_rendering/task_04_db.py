from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        return []

def read_csv_file():
    try:
        products = []
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception as e:
        return []


def read_sqlite_db():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in cursor.fetchall()]
        conn.close()
        return products
    except Exception as e:
        return []


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    elif source == 'sql':
        products = read_sqlite_db()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
