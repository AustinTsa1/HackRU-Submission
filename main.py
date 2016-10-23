from flask import Flask, request, render_template
import twilio.twim1
#import getSchedule.py ?
#import string_manipulation.py ?

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def checklist():
	number = request.form['From']
	message_body = request.form['Body']
	//INSERT CODE TO SPLIT UP MESSAGE BODY

	//PUT RESULTING ARRAY IN A MONGODB DATABASE

	//RESPONSE TO PHONE
	message = getSchedule()

	resp = twilio.twiml.Response()
	resp.message(message)

	return str(resp)

	return render_template("login.html")

@app.route("/<user>")
def index(user=None):
	return render_template("user.html", user=user)

if __name__ = "__main__":
	app.run()

