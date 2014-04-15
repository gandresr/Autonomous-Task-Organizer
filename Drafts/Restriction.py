#-*-coding:utf-8-*-
import datetime

class Restriction(object):
	def __init__(self, start, end, rtype):
		self.start = start #Datetime - Start date of the restriction
		self.end = end #Datetime - End date of the restriction
		self.type = rtype #Type - Type of the restriction
		