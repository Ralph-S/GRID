from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/emergency-override', methods=['POST'])
def emergency_override():
    return jsonify({"status": "Emergency Mode Activated"})

if __name__ == '__main__':
    app.run(debug=True)
