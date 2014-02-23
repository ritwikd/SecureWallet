from os import listdir, urandom, system
from os.path import expanduser
from sys import getsizeof, exit
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
X,Q 	Exit from the thing\n\
C,E		Clear the screen\n\
A,N		Add an item to the screen\n\
L,S 	Display the data for an item\n\
D,R 	Delete an item

"""


if (".securewallet" in listdir(expanduser("~"))):
	dataHandler = open(expanduser("~/.securewallet"), "rb")
	hashedPass = dataHandler.read(32)
	ind = 0;

	while (userPass != hashedPass):
		if (ind > 2):
			print "You have entered an incorrect password 3 times."
			exit()

		else:
			userPass = getpass("Enter your password (" + str(3-ind) + " tries):")

			if (sha256(userPass).digest() == hashedPass):	
				print "Logged in successfully."
				randomIV = dataHandler.read(16)
				cipherData = dataHandler.read()
				plainText = AES.new(sha256(userPass).digest(), AES.MODE_CFB, randomIV).decrypt(cipherData)
				for line in plainText.split('\n')[:-1]:
					splLine = line.split('\xbe')
					userInfo[splLine[0]] = splLine[1:]
				dataHandler.close()

				if (len(userInfo) > 0):
					print "Loaded elements successfully."
					print "Listing elements."
					for i in range(len(userInfo.keys())):
						print str(i+1) + ". "  + userInfo.keys()[i]

				else:
					print "No account data in file."			
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

	elif (userInput in ["x", "exit", "q", "quit"]):
		print "Exiting program."
		done = True

	elif (userInput in ["c", "clear", "e", "empty"]):
		system("clear")

	elif (userInput in ["a", "add", "n", "new"]):
		accName = raw_input("Account Name:")
		userInfo[accName] = [raw_input("Username:"), raw_input("Password:")]
		dataHandler = open(expanduser("~/.securewallet"), "w+")
		dataHandler.write(sha256(userPass).digest())
		randomIV = urandom(16)
		dataHandler.write(randomIV)
		plainText = ""
		
		for key in userInfo.keys():
			plainText = plainText + '\xbe'.join([key, userInfo[key][0], userInfo[key][1]]) + '\n'
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

sys.exit(0)
