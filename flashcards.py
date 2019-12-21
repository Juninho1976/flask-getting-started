from flask import Flask, render_template, abort

from model impobbrt db

app = Flask(__name__)


@app.route("/")
def welcome():
	return render_template("welcome.html",
							cards=db)
	
@app.route("/card/<int:index>")
def card_view(index):
	try:
		card = db[index]
		return render_template("card.html", 
								card=card,
								index=index,
								max_index=len(db)-1)
	except IndexError: 
			abort(404)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)