from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/", methods=["GET", "POST"])
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 10)

    if request.method == "POST":
        guess = int(request.form["guess"])
        if guess == session["number"]:
            result = "You guessed it!"
            session.pop("number")
        elif guess > session["number"]:
            result = "Too high!"
        else:
            result = "Too low!"
        return render_template("index.html", result=result)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)