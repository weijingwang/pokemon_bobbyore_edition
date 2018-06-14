name = raw_input("What is your name?")
	print "Welcome %s!" % (name)

a =raw_input("Pokemon are things")
print "Welcome to the world of POKEMON!!!"
print " As a gift I give you a FREE Mudkip!!!"
pokemon = raw_input("You see a wild Sparrow!!! Do you want to fight it? yes/no")
if pokemon == "yes":
	attack =raw_input("Splash/Mud/Drip/")

	if attack=="Splash":
		print "it died"
		print " you beat the game:"
		print "  ===POKEMON BOBYORE EDITION==="

	elif attack=="Mud":
		print "it died"
		print " you beat the game:"
		print "  ===POKEMON BOBYORE EDITION==="

	elif attack=="Drip":
		print "it died"
		print " you beat the game:"
		print "  ===POKEMON BOBYORE EDITION==="

	else:
		print "You Died."
		print "loser"
		print " you lost the game:"
		print "  ===POKEMON BOBYORE EDITION==="

elif pokemon == "no":
	print "loser"
	print " you lost the game:"
	print "  ===POKEMON BOBYORE EDITION==="

else:
	print "You have just lost the game"
