from flask import Flask, request, jsonify, redirect, url_for, render_template
import mysql.connector
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your_pass",
    database="project"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/store_order_history', methods=['POST'])
def store_order_history():
    orders = request.json if isinstance(request.json, list) else []

    errors = []  
    for idx, order in enumerate(orders):
        dish = order.get('dish')
        quantity = order.get('quantity')
        price = order.get('price')
        timestamp = order.get('timestamp')

        try:
            if isinstance(timestamp, str):
                parsed_time = datetime.strptime(timestamp, '%m/%d/%Y, %I:%M:%S %p')
            else:
                parsed_time = datetime.fromtimestamp(int(timestamp) / 1000)  # assume ms
            cursor.execute("""
                INSERT INTO order_history (dish, quantity, price, order_Time)
                VALUES (%s, %s, %s, %s)
            """, (dish, quantity, price, parsed_time))

        except Exception as e:
            error_msg = f" Failed to store order {idx+1} - Reason: {str(e)}"
            print(error_msg)
            errors.append({"order": idx + 1, "error": str(e)})
            continue
    db.commit()
    print("Saved")


    if errors:
        return jsonify({
            "message": "Some orders failed to store",
            "errors": errors
        }), 400

    return jsonify({"message": "All orders stored successfully"}), 200



if __name__ == '__main__':
    app.run(debug=True)
