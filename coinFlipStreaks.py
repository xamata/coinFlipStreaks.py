'''
# coinFlipStreaks.py
Flip a coin 100 times and create a list with T=tail and H=head.
Write a program that figures out how oftwn a streak of six heads 
	or a streak of six tails comes up in the random list.
Put all of this code in a loop that repeats the experiment
	10,000 times so we can find the percentage of the coin
	flips contains a streak of six heads or tails in a row.
'''
import random
numberOfStreaksHeadsTotal = 0
numberOfStreaksTailsTotal = 0
coin = ('H','T')

# create a function that flips the coin 100 times and creates a list from the results
def coinFlip():
	result = []
	for i in range(0,100):
		if random.randint(0,1) == 0:
			result.append('H')
		else:
			result.append('T')
	resultJoined = ''.join(result)

	numberOfStreaksHeads = 0
	numberOfStreaksTails = 0

	# deteremine how many streaks of six heads or tails comes up within list of 100 flips
	for i in range(len(result)):
		if 'H'*6 in resultJoined[i:i+7]:
			numberOfStreaksHeads += 1
		elif 'T'*6 in resultJoined[i:i+7]:
			numberOfStreaksTails += 1

	# Uncomment to see the results 
	# print(resultJoined)
	# print(str(numberOfStreaksHeads) + 'and \n' + str(numberOfStreaksTails))

	#return the counted streak number for heads and tails
	return numberOfStreaksHeads, numberOfStreaksTails



setCounter = 0
numberOfSets = 10000
for i in range(numberOfSets):	
	# collect the output from a set of 100 flips
	numberOfStreaksHeads, numberOfStreaksTails = coinFlip()

	# grab the total number of streaks
	numberOfStreaksHeadsTotal += numberOfStreaksHeads
	numberOfStreaksTailsTotal += numberOfStreaksTails

# Print out the gathered data
numberOfTimesCoinFlipped = numberOfSets * 100
print(f'Number of times the coin was flipped: {numberOfTimesCoinFlipped}')
print(f'Number of times Heads appeard six times in a row: {numberOfStreaksHeadsTotal}')
print(f'Number of times Tails appeard six times in a row: {numberOfStreaksTailsTotal}')
print()
pecentageStreaksHeads = numberOfStreaksHeadsTotal / numberOfTimesCoinFlipped * 100
pecentageStreaksTails = numberOfStreaksTailsTotal / numberOfTimesCoinFlipped * 100
print(f'Heads appered six times in a row {round(pecentageStreaksHeads,4)}% of the time.')
print(f'Tails appered six times in a row {round(pecentageStreaksTails,4)}% of the time.')