import argparse


def ascii_table():
	for c in range(256):
		print("HEX: {} | DEC: {} | ASCII: {}".format(hex(c), c, chr(c)))


def ascii_to_dec_hex(EXIT_COMMANDS):
	user_in = ""
	while user_in not in EXIT_COMMANDS:
		user_in = input("ASCII: ")
		for ch in user_in:
			try:
				user_in_dec = ord(ch)
				user_in_hex = hex(user_in_dec)
				print("ASCII: {} | DEC: {} | HEX: {}".format(
					ch, user_in_dec, user_in_hex
					))
			except ValueError as ve:
				if user_in not in EXIT_COMMANDS:
					print("Error: {}".format(ve))
				else:
					pass


def dec_to_hex_ascii(EXIT_COMMANDS):
	user_in = ""
	while user_in not in EXIT_COMMANDS:
		user_in = input("DEC: ")
		try:
			user_in_dec = int(user_in)
			user_in_hex = hex(user_in_dec)
			print("DEC: {} | HEX: {} | ASCII: {}".format(
				user_in_dec, user_in_hex, chr(user_in_dec)
				))
		except ValueError as ve:
			if user_in not in EXIT_COMMANDS:
				print("Not a valid decimal number!")
			else:
				pass


def hex_to_dec_ascii(EXIT_COMMANDS):
	user_in = ""
	while user_in not in EXIT_COMMANDS:
		user_in = input("HEX: ")
		try:
			user_in_dec = int(user_in, 16)	# Hex base = 16
			print("HEX: {} | DEC: {} | ASCII: {}".format(
				user_in, user_in_dec, chr(user_in_dec)
				))
		except ValueError as ve:
			if user_in not in EXIT_COMMANDS:
				print("Not a valid hex decimal!")
			else:
				pass
		except OverflowError as ov:
			print("[Error!] - Value to big!")
			print(ov)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", '--input', type=str.lower, 
						choices=['hex', 'ascii', 'ascii-table', 'dec'],
						help="The sort off input value you will give. Default is hex")
	parser.add_argument("-n", '--no-exit', action='store_true',
						help="Disable all the exit commands you would need to exit using ctrl+c")

	"""
	Input types; hex, ascii, dec
	Default = hex

	args.input
	args.no_exit
	"""

	args = parser.parse_args()

	if args.no_exit == True:
		EXIT_COMMANDS = [None]
	else:
		# If any off these are given as input shut down the program
		EXIT_COMMANDS = [':q', ':quit', ':e', ':exit', ':c', ':close']


	print("Startup args:")
	print("Input = {}".format(args.input))
	print("no-exit = {}".format(args.no_exit))
	print("Starting hex_converter!")
	print("Available exit commands: {}".format(EXIT_COMMANDS))
	print("----")

	if args.input == 'hex' or args.input == None:
		hex_to_dec_ascii(EXIT_COMMANDS)
	elif args.input == 'dec':
		dec_to_hex_ascii(EXIT_COMMANDS)
	elif args.input == 'ascii':
		ascii_to_dec_hex(EXIT_COMMANDS)
	elif args.input == 'ascii-table':
		ascii_table()

	else:
		print("Error: {} is not a valid input type!")
		print("Valid types are hex, ascii or dec")
	return 0


if __name__ == '__main__':
	main()
