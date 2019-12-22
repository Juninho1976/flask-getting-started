from flask import 	(Flask, render_template, abort, jsonify, request,
					redirect, url_for)

from model import db,save_db

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


@app.route("/api/card/<int:index>")
def api_card_detail(index):
	try:
		return db[index]
	except IndexError:
		abort(404)
		
@app.route("/api/card/")
def api_card_list():
	return jsonify(db)
	
@app.route("/add_card", methods=["GET", "POST"])
def add_card():
	if request.method == "POST":
		# form submitted
		card = 	{"question" : request.form['question'], 
				"answer" : request.form['answer']}
		db.append(card)
		save_db()
		return redirect(url_for('card_view', index=len(db)-1 ))
	else:
		return render_template("add_card.html")

@app.route("/del_card/<int:index>", methods=["GET", "POST"])
def del_card(index):
	try:
		card = db[index]		
		if request.method == "POST":
			# form submitted
			db.pop(index)
			save_db
			return redirect(url_for('welcome'))
		else:
			return render_template("del_card.html",
									card=card)
	except IndexError:
			abort(404)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
   
   