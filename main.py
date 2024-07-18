from flask import Flask, render_template, redirect
import json

app = Flask(__name__)

@app.route("/")
def root():
    with open("data/orders.json") as orders_file:
        orders = json.load(orders_file)
    orders["nbb"] = "poopsie"

    with open("data/orders.json", "w") as orders_file: 
        json.dump(orders, orders_file)

    return render_template("index.html", orders=orders)

@app.route("/add")
def add_order():
    with open("data/orders.json") as orders_file:
        orders = json.load(orders_file)
    
    orders["nbb"] = "poopsie"

    with open("data/orders.json", "w") as orders_file: 
        json.dump(orders, orders_file)
    
    return ""

if __name__ == "__main__":
    app.run(debug=True, port=9500)