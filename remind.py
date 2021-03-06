from datetime import datetime
import sched, time

def populate(number, event):
	start_time = event[2] #start time is third value in array
	start_time.strip()
	if ("pm" in start_time):
		start_hour = 12
	else:
		start_hour = 0
	
	start_time.replace(start_time,'P','').replace(start_time,'M','').replace(start_time,'A','').replace(start_time,'p','').replace(start_time,'m','').replace(start_time,'a','')
	start_hour = start_hour + int(start_time[:start_time.index(":")])
	start_minute = int(start_time[start_time.index(":"):])
	
	#time_before_alert = int(event[5].strip)
	
	#month = (event[4][:event[4].index("/")]).strip()
	#day = (event[4][event[4].index("/"):]).strip()
	year = time.now().year
	
	timestamp = time.strptime(event[4] + "/" + year + " " + start_hour + ":" + start_minute, "%m/%d/%y %h:%m")
	timestamp = timestamp - (30 * 60)
	
	s.enterabs(timestamp, 1, send_alert, arguments = (event, number)) 


def send_alert(event, number):
	alert = "Reminder: You have an event, " + event[0] + " in 30 minutes."
	resp = twiml.Response()
	resp.message(alert)
	return str(resp)	

