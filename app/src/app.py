from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

if __name__ == '__main__':
    app.run(debug=True)
