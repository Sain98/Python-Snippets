import random

# Tested with python version 3.6

def computer_choice():
	# Get the computer's choice:
	# cmp_choice = random.randint(1, 3)
	# return cmp_choice
	return random.randint(1, 3)

def user_choice():
	# Get user input:
	# Also making sure he inputs a integer (number)
	try:
		choice = int(input("Choice: "))
	except ValueError:
		# no valid number, you can choose how to handle it
		# Im lazy so i just let it set a number for the user
		print("Not a number")
		choice = 1

	# Return the user's input so we can store it
	return choice

def get_outcome(u_choice, cmp_choice):
	# Rock < Paper < Scissors < Rock
	# 1: 'Rock', 2: 'Paper', 3: 'Scissors'
	u_win = {1: 3, 2: 1, 3: 1}	# Rock beats Scissors, Paper beats Rock, Scissors beat Paper

	if u_choice == cmp_choice:
		print("It is a tie!")
		return 'tie'	# Outcome is a tie

	elif cmp_choice == u_win[u_choice]:
		# Ex. If the user has 1 (Rock) and the cmp has option 3 (Scissors)
		# The user wins (Rock > Scissors)
		print("It is a win!")
		return 'win'	# Congratz you won

	else:
		print("It is a loss!")
		return 'lose'	# You lost


def set_score(score, outcome):
	if outcome == 'win':
		score = score + 1

	elif outcome == 'lose':
		score = score - 1

	elif outcome == 'tie':
		score = score - 0.5

	return score


def main():
	end_loop = False
	score = 0
	options = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

	while not end_loop:
		# First we get the user's choice
		print("Please choose a number:\n{}".format(options))
		u_choice = user_choice()


		# Then the computer's choice:
		cmp_choice = computer_choice()
		print("The computer chose : {}".format(options[cmp_choice] ) )
		# The number generated by computer_choice() is 1, 2 or 3
		# These numbers are defined inside the dictionary called options
		# if i call options[1] it will return 'Rock'
		# https://docs.python.org/3.6/tutorial/datastructures.html

		# Checking both choices to see who won
		outcome = get_outcome(u_choice, cmp_choice)

		# We got the outcome now we can edit the score
		score = set_score(score, outcome)

		# Game ended ask user for another round, also display score
		print("\nScore: {}".format(score))
		print("Do you want to keep playing? (y/n)")

		repeat = input("Y\\N: ").lower()

		if repeat != 'y':
			# User wants to stop:
			end_loop = True

	return 0


if __name__ == '__main__':
	main()
