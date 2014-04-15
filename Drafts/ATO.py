#-*-coding:utf-8-*-
import datetime
import User
from math import ceil


class ATO(object):
	def __init__(self):
		
		#self.theta = []
		self.user = User.User()
		self.restrictions = []

	def addRestriction(self, restriction):
		self.restrictions.append(restriction)

	def isCrossedWith(self, starDate, endDate):
		for r in self.restrictions:
			if(r.start <= startDate <= r.end) or (r.start <= endDate <= r.end) or (startDate <= r.start <= endDate): 
				return r
		for t in self.user.tasks:
			if(t.start <= startDate <= r.end) or (r.start <= endDate <= r.end) or (startDate <= r.start <= endDate): 
				return r
		return -1

	def setIntervalStart(self, iduration, istart = datetime.datetime.now()):
		
		d = istart + iduration
		restriction = isCrossed(istart, d)
		if (restriction == -1):
			return istart			
		else:
			istart = restriction.end
			return setIntervalStart(self, iduration, istart)

	def 

	'''
	def organizeTasks(tasks):
		tasks.sort(key=lambda x: x.deadline, reverse = False)
		for task in tasks:
			
			delta_available = task.deadline - datetime.datetime.now()
			days_available = int( delta_available.total_seconds() / datetime.timedelta(days=1).total_seconds() )
			constant_duration = task.estimatedTime.total_seconds() / (days_available*2)
			
			new_dates = [datetime.datetime.now()+datetime.timedelta(days=1)*i*j for i in xrange(days_available)] #################
			durations = [constant_duration for i in xrange( days_available )]
			task.addDD(new_date, durations)
		return tasks
	'''