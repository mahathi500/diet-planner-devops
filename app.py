from flask import Flask, render_template, request
from planner import calculate_plan

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/plan", methods=["POST"])
def plan():
    try:
        data = {"age": int(request.form["age"]), "height": float(request.form["height"]),
                "weight": float(request.form["weight"]), "gender": request.form["gender"],
                "activity": request.form["activity"], "goal": request.form["goal"]}
        return render_template("result.html", result=calculate_plan(data))
    except (ValueError, KeyError):
        return render_template("index.html", error="Please enter valid details."), 400

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
