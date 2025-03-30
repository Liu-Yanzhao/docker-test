from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from AWS CI/CD Pipeline! test 4 surely this is the final commit"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
