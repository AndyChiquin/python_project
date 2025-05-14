from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is a project in Python using Flask on DigitalOcean!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
