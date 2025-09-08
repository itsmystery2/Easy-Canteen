Easy Canteen – Food Ordering Web Application

📌 Overview

Easy Canteen is a web-based food ordering and management system built using Flask (Python), MySQL, HTML/CSS/JS, and localStorage. It allows users to place orders online, make payments, and lets the admin monitor, prepare, and track food orders in real-time.

✨ Features

User-friendly interface for food ordering.
Dynamic order cart with quantity and total bill calculation.
UPI QR Code generation for payments.
Real-time order queue management (FCFS scheduling).
Order timers with automatic movement from Running Orders to Order History.
Admin login to manage and track orders.
Database integration (MySQL) for storing completed order history.

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
Database: MySQL
Others: Flask-CORS, LocalStorage

📂 Project Structure

Easy-Canteen/
│
├── app.py                # Flask backend
├── templates/            # HTML templates
│   ├── main.html
│   ├── order.html
│   ├── payment.html
│   ├── admin.html
│   └── adminlogin.html
│
├── static/               # Static files
│   ├── images (dosa, idli, etc.)
│   ├── logo.png
│   └── style.css
│
└── README.md             # Project documentation

⚙️ Installation

Clone this repository:
git clone https://github.com/itsmystery2/easy-canteen.git
cd easy-canteen

Install dependencies:
pip install flask flask-cors mysql-connector-python

Run the Flask app:
python app.py

Open in browser:
http://127.0.0.1:5000/
