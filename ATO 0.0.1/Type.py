#-*-coding:utf-8-*-

# Class Description:
	# Classification that is given restrictions and pending activities.
class Type(object):

	# Constructor of the class
	# Atributes: "periodicity"  -  (Integer) Number of times that the type has been invoked
 	# 			 "title"        -  (String)  Text max. of 40 char that describes the type    
	def __init__(self, title):
		self.title = title
		self.periodicity = 0 
	
	# Input: "newTitle" - String
	# Output: None	
	# Purpose: Change the title of a type to the input "newTitle"
	def editTitle(self, newTitle):
		self.title = newTitle

	# Input: None
	# Output: None
	# Purpose: Increase in one the number of times that a type has been invoked
	def increasePeriodicity(self):
		self.periodicity += 1


