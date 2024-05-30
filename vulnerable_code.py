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

@app.route('/')
def home():
    response = make_response('Hello, Flask!')
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'  # HSTS header
    return response

@app.route('/echo', methods=['GET'])
def echo():
    user_input = request.args.get('input')
    sanitized_input = escape(user_input)  # Sanitize user input to prevent injection attacks
    response = make_response(f'You said: {sanitized_input}')
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'  # HSTS header
    return response

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')  # Run with SSL

