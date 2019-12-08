from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def welcome():
	return render_template("welcome.html",
	message="Rakesh message test!")
	


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)