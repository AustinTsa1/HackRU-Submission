from flask import Flask, request, render_template
import twilio.twim1

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def checklist():
	number = request.form['From']
	message_body = request.form['Body']

	return render_template("login.html")

@app.route("/<user>")
def index(user=None):
	return render_template("user.html", user=user)

if __name__ = "__main__":
	app.run()

