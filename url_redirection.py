import time
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome user!</h1>"

@app.route("/pass")
def passed():
    return "<h1>Congratulations,you've passed</h1>"


@app.route("/fail")
def failed():
    return "<h1>Sorry,you've failed</h1>"



@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        time.sleep(4)
        return redirect(url_for("passed"))
    else:
        time.sleep(4)
        return redirect(url_for("failed"))  
    
if __name__ == "__main__":
    app.run(debug=True)