import time
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/Welcome")
def welcome():
    return "<h1>Welcome</h1>"


@app.route("/passed/<sname>/<int:num>")
def passed(sname,num):
    return f"<h1>Congratulations {sname.title()},you've passed with {num} marks!"

@app.route("/failed/<sname>/<int:num>")
def failed(sname,num):
    return f"<h1>Sorry {sname.title()},you've failed with {num} marks</h1>"


@app.route("/score/<name>/<int:marks>")
def score(name,marks):
    if marks<30:
        time.sleep(2)
        return redirect(url_for("failed",sname = name,num= marks))
    else:
        return redirect(url_for("passed",sname = name,num = marks))

if __name__ == "__main__":
    app.run(debug=True)
    