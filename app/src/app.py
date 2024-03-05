from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/toggle-cam', methods=['POST'])
def toggle_cam():
    # This is where you handle the toggle
    # For now, let's just return a simple JSON
    return jsonify({"status": "CAM toggled"})

@app.route('/toggle-thermal', methods=['POST'])
def toggle_thermal():
    # Handle the thermal toggle here
    return jsonify({"status": "Thermal toggled"})

if __name__ == '__main__':
    app.run(debug=True)
