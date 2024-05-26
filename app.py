from flask import Flask, request
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/quote')
def quote_text():
    text = request.args.get('text', 'default text')
    quoted_text = quote(text)
    return f'Quoted text: {quoted_text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
