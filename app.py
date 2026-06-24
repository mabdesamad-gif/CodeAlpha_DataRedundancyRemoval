from flask import Flask, render_template, request, jsonify
from validator import add_record
from database import get_all_records

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    result = add_record(data["name"], data["email"], data["phone"])
    return jsonify(result)

@app.route("/records")
def records():
    rows = get_all_records()
    data = [{"id": r[0], "name": r[1], "email": r[2], "phone": r[3], "created_at": r[5]} for r in rows]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)