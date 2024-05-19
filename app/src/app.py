from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

IMAGE_FOLDER = '/home/ralph/Desktop'

@app.route('/emergency-override', methods=['POST'])
def emergency_override():
    data = request.get_json()
    new_state = data.get('state', 'Unknown')

    if new_state == 'Emergency Override':
        print("Switched to Emergency Override mode")
    elif new_state == 'Automated Mode':
        print("Switched to Automated Mode")
    else:
        print(f"Received undefined state: {new_state}")

    return jsonify({"status": "Success", "newState": new_state})

@app.route('/latest-image', methods=['GET'])
def latest_image():
    # Get the latest image file from the folder
    files = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith('.jpg') or f.endswith('.png')]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(IMAGE_FOLDER, x)), reverse=True)
    
    if files:
        latest_image_path = os.path.join(IMAGE_FOLDER, files[0])
        return send_file(latest_image_path, mimetype='image/jpeg')
    else:
        return jsonify({"error": "No images found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
