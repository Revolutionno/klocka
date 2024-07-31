from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/time')
def get_time():
    now = datetime.now()
    clock = {
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
        "day": [now.day, now.strftime("%A")],
        "month": [now.month, now.strftime("%B")],
        "year": now.year,
        "timezone": "GMT+2",  # Adjust as necessary
        "time": now.strftime("%H:%M:%S"),
    }
    return jsonify(clock)

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
