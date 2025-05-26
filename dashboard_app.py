from flask import Flask, render_template_string
import json, os

app = Flask(__name__)

@app.route("/")
def dashboard():
    file = "product_log.json"
    if os.path.exists(file):
        with open(file) as f:
            data = json.load(f)
    else:
        data = []
    return render_template_string("""
    <h1>PulseTrack AI (Shopify Auto Mode)</h1>
    <table border=1>
    <tr><th>Title</th><th>GTIN</th><th>Price</th><th>Compare At</th><th>Margin</th><th>Status</th></tr>
    {% for p in data %}
    <tr>
        <td>{{p['title']}}</td>
        <td>{{p['gtin']}}</td>
        <td>${{p['price']}}</td>
        <td>${{p['compare_price']}}</td>
        <td>{{p['margin']}}%</td>
        <td>{{p['status']}}</td>
    </tr>
    {% endfor %}
    </table>
    """, data=data)