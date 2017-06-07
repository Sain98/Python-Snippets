import string
import time

# TIME 
start_time = time.time()

__author__ = "_Sain"


def inc_key(key, max_value):
	"""
	@params:
		key = the key array, needs to be incremented after generating the url

		max_value = The maximal value an item in the key can have
			if it reaches this value that item will be reset to 0
			and the next item will be incremented by 1

	@about:
		This function is here only to increment the key keeping the rest off the code
		as clean as possible

		Try version - 50.000 URL's:
			STARTING KEY = [0, 0, 0, 0, 0, 0]
			NEW KEY = [44, 22, 12, 2, 0, 0]
			GENERATED 500000 URL'S IN 2.507999897 SECONDS

		Normal version - 50.000 URL's:
			STARTING KEY = [0, 0, 0, 0, 0, 0]
			NEW KEY = [44, 22, 12, 2, 0, 0]
			GENERATED 500000 URL'S IN 2.45900011063 SECONDS
	"""
	
	# - DEBUG -
	if DEBUG:
		print("-- INCREMENTING KEY --")

	# There doeesnt seem to be a noticeable difference between the try and other version

	# Normal version
	for x in range(len(key)):
		if key[x] >= max_value:
			if DEBUG:
				print("MAX VALUE REACHED FOR KEY ID: {}".format(x))
			key[x] = 0
			if x <= len(key):
				key[x + 1] += 1

	# Try, catch version:
	
	"""
	for x in range(len(key)):
		if key[x] >= max_value:
			if DEBUG:
				print("MAX VALUE REACHED FOR KEY ID: {}".format(x))
			key[x] = 0

			try:
				key [x + 1] += 1
			except IndexError as ie:
				print(ie)
				pass
	"""

	key[0] += 1

	return key

# ===============================
# == END OF INC_KEY() FUNCTION ==
# ===============================

def url_gen(key, MAX_LENGTH):
	"""
	@params:
		key = an array used to get the characters from the variable list 'chars'

		MAX_LENGTH = How long the generated url has to be, dont think i need this anymore
					 Seeing how len(key) will always be the same length as MAX_LENGTH

	@about:
		TinyUrl generator for LeetCode
		See: https://leetcode.com/problems/design-tinyurl/#/description

		Example:
		MAX_LENGTH = 6, - 'http://tinyurl.com/xxxxxx' - replacing x with the generated characters
		possible combinations at length 6 is 62 ** 6 = 56800235584 (Not entirely sure this is correct)

	@return:
	 	Generated url - The url we just generated
		key - The key (incremented)

	"""
	# Base url, generated url will be added to it
	base_url = 'http://tinyurl.com/'

	# variable to save generated url to
	url = ['' for x in range(MAX_LENGTH)]

	# All the available characters for generating
	chars = list(string.ascii_letters) + list(string.digits)

	# Length of all available characters = 61 (inc 0)
	chars_len = len(chars) - 1

	for x, k in enumerate(key):
		url[x] = chars[k]

	key = inc_key(key, chars_len)

	url = base_url + ''.join(x for x in url)

	return url, key

# ===============================
# == END OF URL_GEN() FUNCTION ==
# ===============================

def save_key():
	f = open('key.txt', 'w+')
	f.write(str(KEY))
	f.close()

def load_key():
	try:
		f = open('key.txt', 'r')

		key = f.readline()
		key = key.replace('[', '').replace(',', '').replace(']', '')
		key = key.split()

		for c, x in enumerate(key):
			key[c] = int(x)
	except Exception as ex:
		print(ex)
		return None

	return key

"""
=====================================
=	END OF SAVING/LOADING FUNCTIONS =
=====================================
"""

# == SETTING UP ===

# DEBUG MODE - True = On, False = Off
DEBUG = False

# TESTING;
LOOP_TEST = 500000

KEY = load_key()
if KEY != None:
	# Loaded key lets set the max_length
	MAX_LENGTH = len(KEY)

elif KEY == None:
	# Unable to load key
	# So we load default values
	# Max length for the generated url
	MAX_LENGTH = 6

	# Currently key starts off at 0 every time 
	# But if preffered it should be easy to implement a method to write the key to a file or something
	# and set it to the saved value on launch
	KEY = [0 for x in range(MAX_LENGTH)]


# === ... TESTING ... ===

print("STARTING KEY = {}".format(KEY))

for x in range(LOOP_TEST):
	url, KEY = (url_gen(KEY, MAX_LENGTH))

print("NEW KEY = {}".format(KEY))

# Save the updated key afterwards so it can continue and not make already generated url's
save_key()

end_time = time.time()

print("GENERATED {} URL'S IN {} SECONDS".format(LOOP_TEST, (end_time - start_time)))