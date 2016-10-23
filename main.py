from flask import Flask, request, render_template
import twilio.twim1
#import getSchedule.py ?
#import string_manipulation.py ?

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


	#return render_template("login.html")

@app.route("/<user>")
def index(user=None):
	return render_template("user.html", user=user)

if __name__ = "__main__":
	app.run()

