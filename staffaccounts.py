# This script is intended to reduce the time required in account creation for
# new employees by automating most of the creation and requiring the neccessary 
# inputs only once
# 
# Written for Python 2.7 and depends on the following:
#
# Use at your own risk, no liability assumed. Released under the MIT license.
# for more info see https://github.com/rmduddy/staffaccounts

import datetime
import config as cfg

class Employee:
	
	def __init__(self):
		self.firstname = ""
		self.lastname = ""
		self.site = ""
		self.distributionlists = []
		self.schoologyrole = ""
	
	def primaryemail(self):
		primaryemail = "%s%s%s" % (
			self.firstname[:1], self.lastname, cfg.domains['primary']
			)
		return primaryemail.lower()
		
	def secondaryemail(self):
		secondaryemail = "%s%s%s" % (
			self.firstname, self.lastname, cfg.domains['secondary']
			)
		return secondaryemail.lower()
		
	def schoologyaccount(self):
		schoologyaccount = self.primaryemail()
		return schoologyaccount
		
	def password(self):
		password = cfg.passwordgenerator(self.firstname, self.lastname)
		return password

def get_employee_info():

	employee = Employee()

	employee.firstname = raw_input("First name of new employee:")
	employee.lastname = raw_input("Last name of new employee:")
		
	print ("First name: %s" % employee.firstname)
	print ("Last name:  %s" % employee.lastname)
	print ("Primary:    %s" % employee.primaryemail())
	print ("Secondary:  %s" % employee.secondaryemail())
	print ("Schoology:  %s" % employee.schoologyaccount())
	print ("Password:   %s" % employee.password())
	return employee;
	
def main():
	get_employee_info()
	return;

main()
