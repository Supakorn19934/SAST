# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, Flask!'

# @app.route('/echo', methods=['GET'])
# def echo():
#     user_input = request.args.get('input')
#     return f'You said: {user_input}'

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, escape

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, Flask!'

# @app.route('/echo', methods=['GET'])
# def echo():
#     user_input = request.args.get('input')
#     sanitized_input = escape(user_input)  # Sanitize user input to prevent injection attacks
#     return f'You said: {sanitized_input}'

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, escape, make_response

app = Flask(__name__)

# Configuration for HSTS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

@app.after_request
def apply_hsts(response):
    hsts_value = f"max-age={SECURE_HSTS_SECONDS}"
    if SECURE_HSTS_INCLUDE_SUBDOMAINS:
        hsts_value += "; includeSubDomains"
    response.headers['Strict-Transport-Security'] = hsts_value
    return response

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/echo', methods=['GET'])
def echo():
    user_input = request.args.get('input')
    sanitized_input = escape(user_input)  # Sanitize user input to prevent injection attacks
    return f'You said: {sanitized_input}'

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')  # Run with SSL


