from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome! Go to <a href='/items'>/items</a> to see the items list.</h1>"


@app.route('/items')
def show_items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = []

    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

