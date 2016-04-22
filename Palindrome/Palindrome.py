def is_palindrome(word):
	return word == word[::-1]


def is_palindrome_number(num):
	return num == int(str(num)[::-1])
	
	
T = int(raw_input())
i = 0

while i < T:
	i += 1
	
	# test for string
	cmd = raw_input()
	print is_palindrome(cmd)
	
	# test for number
	tmp = int(raw_input())
	print is_palindrome_number(tmp)