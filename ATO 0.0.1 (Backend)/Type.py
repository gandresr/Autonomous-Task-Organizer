#-*-coding:utf-8-*-

#---------Constants-------#
MINIMUM_TIME = 20         # (Integer) - Minimum interval time for a type.

'''
	Class Description:
	# Classification that is given for restrictions and pending activities.
'''
class Type(object):

	'''
	Constructor of the class

	# Atributes: "periodicity"  -  (Integer) Number of times that the type has been invoked
 	# 			 "title"        -  (String)  Text max. of 40 char that describes the type  
 	#			 "priority" 	-  (Integer) Number related with the priority of a task. [0,10]
 	#							   0 is the less important, 10 the most important.
 	'''
	def __init__(self, title, priority):
		self.title = title
		self.periodicity = 0 
		self.priority = priority
	
	'''
		Input: "newTitle" - String
		Output: None	
		Purpose: Change the title of a type to the input "newTitle"
	'''
	def editTitle(self, newTitle):
		self.title = newTitle

	'''
		Input: None
		Output: None
		Purpose: Increase in one the number of times that a type has been invoked
	'''
	def increasePeriodicity(self):
		self.periodicity += 1


