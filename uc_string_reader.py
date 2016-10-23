import datetime
import calendar
import time

#SAMPLE_INPUT -> "going to the casc for hackru at 10:00 to 12:00 todayu"

def read_string(uc_string):
	array = uc_string.split(" ")
	if(triggered(uc_string) == 'true'):
		start_time = find_start_time(array)
		end_time = find_end_time(array)
		title = find_title(array)
		location = find_location(array)
		date = find_date(array)
		x = (str(title+","+location+","+start_time+","+end_time+","+date+","+"30"))
		return x

def find_start_time(array):
	for a in array:
		if(':' in a):
			x = a

			return str(x)
	return "ERROR"

def find_end_time(array):
	counter = 2
	for a in array:
		if(':' in a and counter == 1):
			x = a
			return str(x)
		elif(':' in a and counter == 2):
			counter = 1
			
	return "ERROR"

def find_date(array):
	month = "";
	date = "";
	for a in array:
		if(a == 'tomorrow'):
			timeNow = datetime.datetime.now()
			anotherTime = timeNow + datetime.timedelta(days=1)
			date = anotherTime.strftime("%d")
			month = anotherTime.strftime("%B")
		elif(a == 'today'):
			date = time.strftime("%d")
			month = time.strftime("%B")
		else:	
			array1 = []
			for a in array:
				if('/' in a):
					array1 = a.split("/")
					date = array1[1]
					month = calendar.month_name[int(array1[0])]
	x = month+" "+date
	return(str(x))

def find_location(array):
	full_location = ""
	adding = 0;
	for a in array:
		if(a == 'to' and adding == 0):
			adding = 1
		elif(a != 'for' and adding == 1):
			full_location += " "
			full_location += a
		elif(a == 'for' and adding == 1):
			adding = 0
			full_location = full_location[:0] + full_location[(0+1):]
			return str(full_location)

def find_title(array):
	full_title = ""
	adding = 0;
	for a in array:
		if(a == 'for' and adding == 0):
			adding = 1
		elif(a != 'at' and adding == 1):
			full_title += " "
			full_title += a
		elif(a == 'at' and adding == 1):
			adding = 0
			full_title = full_title[:0] + full_title[(0+1):]
			return str(full_title)

def triggered(array):
	triggers = ['meet', 'event', 'hang', 'going']
	for a in array:
		for b in triggers:
			if(a == b):
				return 'true'
	return 'false'

