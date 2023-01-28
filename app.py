from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    visitor_ip = request.remote_addr
    visitor_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitor_data = f'IP: {visitor_ip}, Time: {visitor_time}'
    #Log the visitor data to a file or database
    with open("visitor_log.txt", "a") as f:
        f.write(visitor_data + '\n')
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
