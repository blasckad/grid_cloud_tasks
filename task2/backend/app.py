from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello from the backend!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
