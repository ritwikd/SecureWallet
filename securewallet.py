from os import listdir, urandom, system
from os.path import expanduser
from Crypto.Cipher import AES
from hashlib import sha256
from getpass import getpass

done = False
userPass = ""
userInfo = {}
hashedPass = ""
accName = ""
randomIV = ""
helpData = """H - Display the help Page\n\
X - Exit from the thing\n\
C - Clear the screen\n\
A - Add an item to the screen\n\
"""


if (".securewallet" in listdir(expanduser("~"))):
	dataHandler = open(expanduser("~/.securewallet"), "r")
	
	hashedPass = dataHandler.read(32)
	dataHandler.close()
	ind = 0;
	while (userPass != hashedPass):
		if (ind > 2):
			print "You have entered an incorrect password 3 times."
			exit()
		else:
			userPass = getpass("Enter your password (" + str(3-ind) + " tries):")
			if (sha256(userPass).digest() == hashedPass):
				break
				print "Logged in successfully."
				system("clear")
			else:
				print "Incorrect password."
				ind += 1
else:
	same = False
	while not same:
		userPass = getpass("Enter a password for your data:")
		userPass2 = getpass("Confirm password:")
		if (userPass == userPass2):
			same = True
		else:
			print "Passwords did not match."

	dataHandler = open(expanduser("~/.securewallet"), "w+")
	dataHandler.write(sha256(userPass).digest())
	dataHandler.close()



while not done:
	userInput = raw_input("Enter a command (H for help):").lower()
	if (userInput in ["h", "help"]):
		print helpData

	elif (userInput in ["x", "exit"]):
		print "Exiting program."
		done = True

	elif (userInput in ["c", "clear"]):
		system("clear")

	elif (userInput in ["a", "add", "n", "new"]):
		accName = raw_input("Account Name:")
		userInfo[accName] = [raw_input("Username:"), raw_input("Password:")]
		dataHandler = open(expanduser("~/.securewallet"), "w+")
		dataHandler.write(sha256(userPass).digest())
		randomIV = os.urandom(16)
		t = '\xbe'  
		dataHandler.close()

	elif (userInput in ["l", "list", "s", "show", "v", "view"]):
		print "Listing elements"
		print '\n'.join(userInfo.keys())
	
	else:
		print "Unrecognized command."

exit()
