from flask import Flask, render_template, request
from malicious_url_detection_and_fraud_phone_number_detection import (
    predict_url,
    predict_phone_number,
)

app = Flask(__name__)


@app.route("/url", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        result = predict_url(url)
        return render_template("index.html", result=result)
    return render_template("index.html")


@app.route("/toll_free", methods=["GET", "POST"])
def toll_free():
    if request.method == "POST":
        toll_free = request.form["toll_free"]
        result = predict_phone_number(toll_free)
        return render_template("index.html", result=result)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
