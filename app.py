from flask import Flask

app = Flask(__name__)


@app.route("/")
def quick_setup():
    return "Quick setup"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
