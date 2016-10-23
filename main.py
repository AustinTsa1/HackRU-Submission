from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def checklist():
	return render_template("a.html")

if __name__ = "__main__":
	app.run()

