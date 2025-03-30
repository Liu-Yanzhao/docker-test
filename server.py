from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>please work please work please work please work 2</h1>" \
           '<img src="/image/image.png" alt="My Image" width="300">'

@app.route("/image/<filename>")
def get_image(filename):
    return send_from_directory("static/images", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

