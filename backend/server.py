from flask import Flask, send_file, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_image/<image_name>')
def get_image(image_name):
    print(image_name)
    return send_file(f'image/{image_name}', mimetype='image/png') # Correct mimetype

@app.route('/get_chat_response', methods=['POST'])
def get_chat_response():
    data = request.json
    user_text = data.get('text', '')
    response_text = f"I heard you say {user_text}"
    return jsonify({'response': response_text})

if __name__ == "__main__":
    print("Starting Flask Server")
    app.run(debug=True)

