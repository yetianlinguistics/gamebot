from flask import Flask, send_file, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
# CORS(app, origins='*', methods='*', allow_headers=['Content-Type'])
# CORS(app, origins=['http://localhost:8000'], methods='*', allow_headers=['Content-Type'], supports_credentials=True)

CORS(app, origins='*', methods=['POST', 'OPTIONS'], allow_headers=['Content-Type', 'Authorization'], supports_credentials=True)


@app.route('/get_image/<image_name>')
def get_image(image_name):
    print(image_name)
    return send_file(f'image/{image_name}', mimetype='image/png') # Correct mimetype

# @app.route('/get_chat_response', methods=['POST'])
# def get_chat_response():
#     data = request.json
#     user_text = data.get('text', '')
#     response_text = f"I heard you say {user_text}"
#     return jsonify({'response': response_text})

@app.route('/get_chat_response', methods=['POST', 'OPTIONS'])
def get_chat_response():
    if request.method == 'OPTIONS':
        print("Received an OPTIONS request.")
        # Here you can set up your custom headers for the preflight
        response = app.make_default_options_response()
        return response

    print("Request Headers:", request.headers)

    if request.is_json:
        data = request.get_json()
        user_text = data.get('text', '')
        response_text = f"I heard you say {user_text}"
        return jsonify({'response': response_text})
    else:
        return "Unsupported Media Type", 415


if __name__ == "__main__":
    print("Starting Flask Server")
    app.run(debug=True, port=15007)

