#-*-coding:utf-8-*-
import datetime
#-*-coding:utf-8-*-
import datetime 

class Task(object):
	def __init__(self, new_deadline, new_estimatedTime, new_title, new_description, new_priority):
		if ( new_deadline - datetime.datetime.now() ) > datetime.timedelta(hours=new_estimatedTime[0], minutes=new_estimatedTime[1], seconds=new_estimatedTime[2]):
			self.deadline = new_deadline #datetime - Deadline to complete the task
			# Time - Time estimated to complete the task
			# new_estimated_time is a tuple (h,m,s)
			self.estimatedTime = datetime.timedelta(hours=new_estimatedTime[0], minutes=new_estimatedTime[1], seconds=new_estimatedTime[2])
			self.title = new_title #String - Máx 25 char
			self.description = new_description #String - Máx 200 char
			self.startDates = [] #List - List of datetimes of size n
			self.durations = [] #List - List of timedeltas
			# Integer - Level of priority
			# Dead Serious = 2
			# Important = 1
			# Regular Task = 0
			self.priority = new_priority 
			#############self.type = Type(..........)#########
		else:
			raise Exception("Are you kidding me?")

	#Add new date and duration (It represents a new interval of time to work in the task)
	def addDD(self, new_dates, new_durations):
		self.startDates += new_dates
		self.durations += new_durations

	#Change date and duration
	def changeDD(self, new_date, new_duration, date_index):
		self.startDates[date_index] = new_date
		self.durations[date_index] = new_duration


