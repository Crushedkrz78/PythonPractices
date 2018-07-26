"""
This is a script used to test the python interpreter
installed on a Virtual Machine using Ubuntu 18.04

This script was created to update  the Python
Repository on my Github Account
"""

#Checks a file where is saved the number of script runs
with open("opening.txt","r+") as check:
	opening = check.readline()
	if  opening != '':
		opening = int(opening)
	else:
		opening = 0
	#Shows a banner where is displayed the number of script openings
	print "Hello!! this script has been executed %s times before" % opening
	if opening == 0:
		print "So this is the first run!!"

	#Asks for a String to display a message on Terminal
	message = str(raw_input("Insert a message to display:\n"))

	#Asks for a number of repetitions for the message
	repMsg = int(raw_input("Insert a number of repetitions to do:\n"))
	i = 1

	while(i<=repMsg):
		print 'Message: %s \n - Repetition Number: %s' % (message, i)
		i+=1
	opening += 1
	check.close()

with open("opening.txt","w") as check:
	check.write(str(opening))

#End of file

