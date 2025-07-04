<<<<<<< HEAD
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ThePacificEdu - AI chatbot for underserved learners."
    })

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ThePacificEdu - AI chatbot for underserved learners."
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
>>>>>>> 4d2e7eeb6b35c195a7d74d3cacc74ba11752ae36
