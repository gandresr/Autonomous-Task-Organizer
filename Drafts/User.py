#-*-coding:utf-8-*-
import datetime 
import Task

class User(object):
	def __init__(self): #name, career, birth, email):
		self.name = raw_input('Name: ') #name # String - User name or alias
		self.career = raw_input('Career: ') #career # Integer - code of career
		self.birth = raw_input('Birth: ') #birth # Tuple - Date of birth (dd,mm,yy)
		self.email = raw_input('Email: ') #email # String - email (If the user wants to receive updates email != "")
		self.tasks = [] # List of tasks
		#############self.password#############

	def changeCareer(self, new_career):
		self.career = new_career

	def changeEmail(self, new_email):
		self.email = new_email

	def refreshTasks(self):
		for task in self.tasks:
			if task.deadline < datetime.datetime.now():
				self.tasks.remove(task)

	def crossedDate(task2verify):
		if len(tasks) > 0:
			for date2verify in task2verify:
				for task in tasks:
					for j in xrange( len(tasks.startDates) ):
						if  task.startDates[j] <= date2verify <= (task.startDates[j] + task.durations[j]):
							return j
		return -1
				
	def addTask(self, new_Task):
		date_index = crossedDate(new_Task)
		if  date_index == -1:
			self.tasks.append(new_Task)
			return 1
		else:
			return -1

