class custom_cycle:
	def __init__(self, user_string):
		self.u_str = user_string
		self.u_str_len = len(self.u_str)
		self.u_str_buff = None

		self.counter = 0


	def next_item(self):
		"""
		Replaces the character in the buffer (u_str_buff) by the next character
		Increases the counter by 1 
		OR resets it to 0 if the counter is at the maximum number
		else it would throw: IndexError: string index out of range
		"""
		self.u_str_buff = self.u_str[self.counter]

		if self.counter < self.u_str_len:
			self.counter += 1

		if self.counter >= self.u_str_len:
			self.counter = 0

		return self.u_str_buff


	def get_counter(self):
		"""
		Returns the integer counter
		"""
		return self.counter



#################
# TESTING USAGE #
#################

def main():
	# Testing
	x = custom_cycle('sander')

	print()
	for y in range(50):
		print(x.next_item())


if __name__ == '__main__':
	main()
