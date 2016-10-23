#from flask import Flask 
from flask_pymongo import PyMongo 

#app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'user_schedules_db'
app.config['MONGO_URI'] = 'mongodb://yerdman:hackru2016@ds063946.mlab.com:63946/user_schedules_db'

mongo = PyMongo(app) 

@app.route('/add_user')
def add_user(name,number,event):
	#name = 'Avin'
	#number = '9873049872'
	#event = [1,2,3]
	#events = [event]
	user = mongo.db.user_schedules_db
	user.insert({'name' : name, 'number' : number,'events' : events})
	return 'Added User!'

@app.route('/add_event')
def add_event(number,event):
	#number = '9873049872'
	#event = [4,5,6]
	user = mongo.db.user_schedules_db
	current = user.find_one({'number' : number})
	current['events'].append(event)
	user.save(current)
	return 'Added Messages!'


@app.route('/get_events')
def get_events(number):
	#number = '9873049872'
	user = mongo.db.user_schedules_db
	try:
		current = user.find_one({'number' : number})
		return(str(current['events']))
	except Exception as e:
		return("ERROR")
	else:
		pass
	finally:
		pass

@app.route('/get_name')
def get_name(number):
	#number = '9873049872'
	user = mongo.db.user_schedules_db
	try:
		current = user.find_one({'number' : number})
		return(str(current['name']))
	except Exception as e:
		return("ERROR")
	else:
		pass
	finally:
		pass
	

if __name__ == '__main__':
	app.run(debug=True)
  