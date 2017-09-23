import argparse

__author__ = "Sain"
__version__ = 2


def convert(input_type, input_value):
	if input_type == 'hex':
		input_value_dec = convert_value_hex_dec(input_value)
		input_value_ascii = convert_value_to_ascii(input_value_dec)
		input_value_bin = convert_value_to_bin(input_value_dec)

		print("HEX: {} | DEC: {} | BIN: {} | ASCII: {}".format(
			input_value, input_value_dec, input_value_bin, input_value_ascii
			)
		)

	elif input_type == 'dec':
		input_value = convert_value_str_dec(input_value)
		input_value_hex = convert_value_dec_hex(input_value)
		input_value_ascii = convert_value_to_ascii(input_value)
		input_value_bin = convert_value_to_bin(input_value)

		print("DEC: {} | HEX: {} | BIN: {} | ASCII: {}".format(
			input_value, input_value_hex, input_value_bin, input_value_ascii
			)
		) 

	elif input_type == 'ascii':

		for ch in input_value:
			input_value_dec = convert_value_ascii_dec(ch)
			input_value_hex = convert_value_ascii_hex(ch)
			input_value_bin = convert_value_to_bin(input_value_dec).zfill(8)

			print("ASCII: {} | HEX: {} | DEC: {} | BIN: {}".format(
				ch, input_value_hex, input_value_dec, input_value_bin
				)
			)


def convert_value_hex_dec(hex_value):
	try:
		return int(hex_value, 16)	# Hex -> dec (hex is base 16)
	except ValueError as ve:
		print("Not a valid number!")
		return 0

def convert_value_str_dec(src_value):
	try:
		return int(src_value)		# string -> int
	except ValueError as ve:
		print("Not a valid number!")
		return 0

def convert_value_dec_hex(dec_value):
	return hex(dec_value)			# Dec -> hex

def convert_value_to_ascii(src_value):
	return chr(src_value)			# hex, dec -> ascii

def convert_value_to_bin(src_value):
	return bin(src_value)[2:]		# Ignore the '0b'

def convert_value_ascii_hex(src_value):
	return hex(ord(src_value))		# ascii -> hex

def convert_value_ascii_dec(src_value):
	return ord(src_value)			# ascii -> dec


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", '--input', type=str.lower, 
						choices=['hex', 'ascii', 'ascii-table', 'dec'],
						help="The sort off input value you will give. Default is hex")
	parser.add_argument("-n", '--no-exit', action='store_true',
						help="Disable all the exit commands you would need to exit using ctrl+c")
	parser.add_argument("-d", '--direct', action='store_true',
						help="No loop, just directly converts and gives you the result then closes")
	
	"""
	Input types; hex, ascii, dec
	Default = hex

	args.input
	args.no_exit
	args.direct
	"""

	args = parser.parse_args()

	if args.input == None:
		args.input = 'hex'

	if args.no_exit == True:
		exit_commands = [None]
	else:
		exit_commands = [':q', ':quit', ':e', ':exit', ':c', ':close']

	user_in = ""

	if args.direct != True:
		print("Startup args:")
		print("Input = {}".format(args.input))
		print("no-exit = {}".format(args.no_exit))
		print("direct = {}".format(args.direct))
		print("Starting hex_converter!")
		print("Available exit commands: {}".format(exit_commands))
		print("----")

	if args.direct == False:
		while user_in not in exit_commands:
			user_in = input("{}: ".format(args.input.upper()))

			if user_in not in exit_commands:
				convert(args.input, user_in)

	else:
		# args.direct == True
		user_in = input("{}: ".format(args.input))

		convert(args.input, user_in)

	return 0

if __name__ == '__main__':
	main()
