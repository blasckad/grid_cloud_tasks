from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def call_backend():
    try:
        res = requests.get("http://backend-service")
        return f"Frontend received: {res.text}"
    except Exception as e:
        return f"Error contacting backend: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
