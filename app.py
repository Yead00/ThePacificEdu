from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ThePacificEdu - AI chatbot for underserved learners."
    })

if __name__ == "__main__":
    app.run(debug=True)
