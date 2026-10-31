from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, World! Your Flask app is running successfully."})

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Runs the local development server
    app.run(debug=True, host='0.0.0.0', port=5000)
