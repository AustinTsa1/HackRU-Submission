from flask import Flask, request, render_template
import twilio.twim1
from getSchedule import *
from mongodb_access import *
from string_manipulation import *
#imports classes

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def checklist():
	number = request.form['From']
	message_body = request.form['Body']

	if (message_body == "schedule"):
		#RESPONSE TO PHONE; getSchedule() splits up string
		message = getSchedule(get_events(number))

		resp = twilio.twiml.Response()
		resp.message(message)
		return str(resp)	#returns message to user
	else:
		#PUT USERS INFO IN A MONGODB DATABASE
		if (get_events(number) == "ERROR"):
			#if user isn't present in database add user
			add_user(number, string_manipulation(message_body))
		else:
			#if user is present add event
			add_event(number, string_manipulation(message_body))


	#return render_template("login.html")

@app.route("/<user>")
def index(user=None):
	return render_template("user.html", user=user)

if __name__ = "__main__":
	app.run()

