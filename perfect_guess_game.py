import random
randNumer = random.randint(1, 100)
userGuess = None
guesses = 0
while (userGuess != randNumer):
	userGuess = int(input("Enter your guess:"))
	if(userGuess == randNumer):
		print("You guessed it right!")
	else:
		if (userGuess>randNumer):
			print("You guessed it wrong! Enter a smaller number")
		else:
			print("You guessed it wrong! Enter a larger number")
	guesses += 1

print(f"You guessed the number in {guesses} guesses")

with open('hiscore.txt', 'r') as f:
	hiscore = int(f.read())

if(guesses<hiscore):
	print("You have just broken the hiscore!")
	with open('hiscore.txt', 'w') as f:
		f.write(str(guesses))