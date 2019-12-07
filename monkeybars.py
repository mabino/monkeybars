import random
import time

class bcolors:
	BLUE = '\033[94m'
	GREEN = '\033[92;1m'
	RED = '\033[91;1m'
	ENDC = '\033[0m'

def displayIntroduction():
	print(''' You find yourself in a playground with ''' + bcolors.GREEN + '''the best monkey bars in the world''' + bcolors.ENDC + '''. You climb the ladder.''')
	
def chooseSkip():
	skipChoice = ''
	while skipChoice != '1' and skipChoice != '2' and skipChoice != '3':
		print('\nWill you skip one, two, or three bars? Type 1, 2, or 3:')
		skipChoice = input()
	return skipChoice
	
def checkChoice(skipChoice):
	print('\nYou reach out to grab the bar.')
	time.sleep(2)
	print('\nYour fingers just about make it…')
	time.sleep(2)
	print('\nYou jump off the platform and …\n')
	print('_O/')
	print('  \\')
	print('  /\_')
	print('  \   ')
	time.sleep(2)
	
	jumpResult = random.randint(1, 3)
	
	def bigReward():
		print(bcolors.BLUE + '░░░░░░░░░░░░░░░░░░░░░░█████████')
		print('░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███')
		print('░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███')
		print('░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██')
		print('░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███')
		print('░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██')
		print('░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██')
		print('░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██')
		print('░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██')
		print('██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██')
		print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██')
		print('██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██')
		print('░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██')
		print('░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
		print('░░████████████░░░█████████████████')
		print('\n\n------------' + bcolors.ENDC)
		time.sleep(3)
	
	def jumpResultWord(jumpNum):
		switch = {
			1: "first",
			2: "second",
			3: "third"
		}
		return switch.get(jumpNum, "no")
	
	jumpWord = jumpResultWord(jumpResult)
	
	if skipChoice == str(jumpResult):
		print(bcolors.GREEN + 'You it made to the ' + jumpWord + ' bar on the')
		time.sleep(1)
		print(bcolors.GREEN + 'best')
		time.sleep(1)
		print(bcolors.GREEN + 'monkey')
		time.sleep(1)
		print(bcolors.GREEN + 'bars')
		time.sleep(1)
		print(bcolors.GREEN + 'in the WORLD!')
		time.sleep(2)
		if jumpResult == 3:
			bigReward()

	else:
		print(bcolors.RED + 'You missed this time.  But don\'t give up!  Try again!')
		print('\n\n------------' + bcolors.ENDC)

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
		displayIntroduction()
		attempt = chooseSkip()
		checkChoice(attempt)
		print("Do you want to try the bars again? Type yes or no: ")
		playAgain = input()
		print('\n\n\n\n')