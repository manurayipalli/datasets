from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route
@app.route("/")
def home():
    return "Hello, World! 🚀 This is my first Python app."

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
