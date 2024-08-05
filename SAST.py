from flask import Flask, request, escape

app = Flask(__name__)
Talisman(app)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/echo', methods=['GET'])
def echo():
    user_input = request.args.get('input')
    sanitized_input = escape(user_input)  # Sanitize user input to prevent injection attacks
    return f'You said: {sanitized_input}'

if __name__ == '__main__':
    app.run(debug=True)
