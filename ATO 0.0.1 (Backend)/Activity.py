#-*-coding:utf-8-*-
#---------Modules---------#
from datetime import datetime

''' Class Description:
	Abstract class with atributes for different kinds of activities'''
class Activity(object):

	'''
	Constructor of the class

	# Atributes:  "title"             -  (String)    Text max. of 40 char that describes the pending activity.
	#			  "estimatedTime"     -  (timeDelta) It is the time that the user believes that he/she will spend 
	#			  "isCompleted"		  -  (Bool)		 True if the activity has been completed, False if not
	# 			  "type"			  -  (Type)      Type of the pending activity.
	#			  "description"       -  (String)    140 char max. that describes details of the pending activity.
	#			  "deadline"          -  (datetime)  Limit date to end the pending activity.
	#								                 performing a pending activity.
	#			  "startTime"		  -  (datetime)  Date when the activity is createc.
	'''
	def __init__(self, title, estimatedTime, isCompleted, atype, deadline, description=""):
		self.title = title
		self.estimatedTime = estimatedTime
		self.isCompleted = isCompleted
		self.type = atype
		self.description = description
		self.deadline = deadline
		self.startTime = datetime.now()

	'''
		Input: "newDeadline"  (datetime)  -  New deadline for the activity
		Ouput: Raise Exception if the new deadline is lesser or equal than datetime.datetime.now() + the minimum time of a time interval.
		Purpose: Change the deadline of a pending activity.
	'''
	def reschedule(self, newDeadline):
		if( newDeadline > (datetime.now() + TimeInterval.MINIMUM_TIME) ):
			self.deadline = newDeadline
		else:
			raise Exception("The new deadline is too close.")

	'''
		Input: None
		Ouput: Return the attribute isCompleted
		Purpose: It tells if the activity has been completed or not
	'''
	def isCompleted(self):
		return self.isCompleted