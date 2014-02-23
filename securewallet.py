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
	ind = 0;abu
	while (userPass != hashedPass):
		if (ind > 2):
			print "You have entered an incorrect password 3 times."
			exit()
		else:
			userPass = getpass("Enter your password (" + str(3-ind) + " tries):")
			if (sha256(userPass).digest() == hashedPass):	
				print "Logged in successfully."
				dataHandler = open(expanduser("~/.securewallet"), "w+")
				randomIV = dataHandler.read(16)
				cipherData = dataHandler.read()
				plainText = AES.new(sha256(userPass).digest(), AES.MODE_CFB, randomIV).decrypt(cipherData)
				for line in plainText.split('\n'):
					print spl
					splLine = line.split('\xbe')
					userInfo[splLine[0]] = splLine[1:]
				dataHandler.close()
				print "Loaded elements."
				break
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
		randomIV = urandom(16)
		plainText = ""
		for key in userInfo.keys():
			plainText = plainText + '\xbe'.join([key, userInfo[key][0], userInfo[key]][1]) + '\n'
		cipherData = AES.new(sha256(userPass).digest(), AES.MODE_CFB, randomIV).encrypt(plainText)
		dataHandler.write(cipherData)
		dataHandler.close()

	elif (userInput in ["l", "list", "s", "show"]):
		if (len(userInfo) > 0):
			print "Listing elements."
			for i in range(len(userInfo.keys())):
				print str(i+1) + ". "  + userInfo.keys()[i]
		else:
			print "No elements to list."

	elif (userInput in ["v", "view", "d", "display"]):
		
		if (len(userInfo) > 0):
			print "Listing elements."
			for i in range(len(userInfo.keys())):
				print str(i+1) + ". "  + userInfo.keys()[i]
			userInput = input("Choose an item to view: ")
			print userInfo.keys()[userInput-1]
			print "=" * len(userInfo.keys()[userInput-1])
			print "Username:" + userInfo[userInfo.keys()[userInput-1]][0]
			print "Password:" + userInfo[userInfo.keys()[userInput-1]][1]
		else:
			print "No items to view."

	elif (userInput in ["d", "delete", "r", "remove"]):
		if (len(userInfo) > 0):
			print "Listing elements."
			for i in range(len(userInfo.keys())):
				print str(i+1) + ". "  + userInfo.keys()[i]
			userInput = input("Choose an item to view: ")
			del(userInfo[userInfo.keys()[userInput-1]])
		else:
			print "No items to delete."
	
	else:
		print "Unrecognized command."

exit()
