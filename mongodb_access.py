from pymongo import MongoClient
#from flask_pymongo import PyMongo 

#app = Flask(__name__)

mongo = MongoClient('ds063946.mlab.com', 63946)
db = mongo['user_schedules_db']
db.authenticate('admin', 'admin')

#@app.route('/add_user')
def add_user(number,event):
	#number = '9873049872'
	#event = [1,2,3]
	events = [event]
	user = db.user_schedules_db
	user.insert({'number' : number,'events' : events})
	return 'Added User!'

#@app.route('/add_event')
def add_event(number,event):
	#number = '9873049872'
	#event = [4,5,6]
	user = db.user_schedules_db
	current = user.find_one({'number' : number})
	current['events'].append(event)
	user.save(current)
	return 'Added Messages!'


#@app.route('/get_events')
def get_events(number):
	#number = '9873049872'
	user = db.user_schedules_db
	try:
		current = user.find_one({'number' : number})
		return(current['events'])
	except Exception as e:
		return("ERROR")
	else:
		pass
	finally:
		pass
	return 'x'
<<<<<<< HEAD

def remove_events(number):
	user = db.user_schedules_db
	print("HERE")
	db.user_schedules_db.remove({'number': number})
	return 'success'
=======
>>>>>>> 3a20231f98fcbd42df624d069e0911330e211ccf

#if __name__ == '__main__':
#	app.run(debug=True)
