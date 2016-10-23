from flask import Flask, request, render_template
import twilio.twim1
from getSchedule import *
from mongodb_access import *
#imports classes

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def checklist():
	number = request.form['From']
	message_body = request.form['Body']

	if (message_body == "schedule"):
		#RESPONSE TO PHONE; getSchedule() splits up string
		message = getSchedule()

		resp = twilio.twiml.Response()
		resp.message(message)
		return str(resp)	#returns message to user
	else:
		#PUT USERS INFO IN A MONGODB DATABASE
		if (get_name(number) == "ERROR")


	#return render_template("login.html")

@app.route("/<user>")
def index(user=None):
	return render_template("user.html", user=user)

if __name__ = "__main__":
	app.run()

