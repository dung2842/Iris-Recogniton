from flask import Flask, render_template, request
from modules.enrollment import enroll_user
from modules.authentication import authenticate
from modules.fusion import decision
import pickle
import pandas as pd
from flask import send_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/enroll", methods=["GET","POST"])
def enroll():

    if request.method == "POST":

        user = request.form["user"]
        file = request.files["iris"]

        path = "temp.jpg"
        file.save(path)

        enroll_user(user, path)

        return render_template("success.html", user=user)

    return render_template("enroll.html")


@app.route("/authenticate", methods=["GET","POST"])
def auth():

    if request.method == "POST":

        user = request.form["user"]
        file = request.files["iris"]

        path = "temp.jpg"
        file.save(path)

        best_user, score = authenticate(path)

        result = decision(score)

        return render_template(
            "result.html",
            user=best_user,
            score=round(score,3),
            result=result
        )

    return render_template("authenticate.html")

@app.route("/export")
def export_database():

    with open("database/features.pkl","rb") as f:
        db = pickle.load(f)

    rows = []

    for user, feature in db.items():

        row = {"user": user}

        for i,v in enumerate(feature):
            row[f"f{i}"] = v

        rows.append(row)

    df = pd.DataFrame(rows)

    file_path = "database/iris_database.xlsx"

    df.to_excel(file_path, index=False)

    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)