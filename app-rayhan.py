from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, t'y prends pas à la dernière"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
