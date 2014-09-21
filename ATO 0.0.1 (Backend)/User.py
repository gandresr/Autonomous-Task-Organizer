#-*-coding:utf-8-*-
#---------Modules---------#
import datetime

#---------Constants-------#
CAREERS = ['Student', 'Manager', 'Independent Worker']  # (List) - List of careers.

# Class Description:
	# Person with difficulties to organize his/her tasks. 
class User(object):

	'''
	Constructor of the class

	# Inputs:     "dbirth"    -  (Integer)  * User's day of birth   [1,31]
	#			  "mbirth"    -  (Integer)  * User's month of birth [1,12]
	# 			  "ybirth"    -  (Integer)  * User's year of birth  [0,99999]
	# Atributes:  "username"  -  (String)   * User's name
	#			  "password"  -  (String)   * User's personal coded password
	#			  "careers"   -  (List)     * User's careers. List of indexes related with CAREERS.
	#			  "friends"   -  (List)     * The usernames of the User's friends or colleagues
	#			  "license"   -  (Integer)  * 0 if the user has a free license / 1 if the user has a paid license
	#			  "email"     -  (String)   * Email of the user - <useremail@something>
	#			  "birthday"  -  (datetime) * User's birthday
	#			  "accuracy"  -  (float)    * User's accuracy to determine the time that he/she is going to spend
	#										  doing some pendind activity.
	# If the career is not in the db it is saved.
	'''
	def __init__(self, username, password, careers, email, dbirth, mbirth, ybirth, license = 0, friends = []):
		self.username = username
		self.password = password
		self.careers = []
		for career in careers:
			if( career in CAREERS ):
				self.careers.append( CAREERS.index(career) )
			elif( raw_input("Do you want to add your career to our db? (y/n) ") == "y" ):
				CAREERS.append(career)
				self.careers.append( CAREERS.index(career) )
		self.friends = friends
		self.license = license
		self.email = email
		self.birthday = datetime.datetime( ybirth, mbirth, dbirth )

		
		