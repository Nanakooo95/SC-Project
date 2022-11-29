"""
File: largest_digit.py
Name: Yi Lin Yang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the given number
	:return:
	"""
	# make n a natural number
	if n < 0:
		n = -n
	if n // 10 == 0:
		return n
	else:
		return max(find_largest_digit(n//10), find_largest_digit(n%10))

# 	largest_digit = 0
# 	return find_largest_digit_helper(n, largest_digit)
#
#
# def find_largest_digit_helper(n, largest_digit):
#
# 	# base case: unit digit number
# 	if n < 10:
# 		if largest_digit > n:
# 			return largest_digit
# 		else:
# 			return n
# 	# recursive
# 	else:
# 		if n % 10 > largest_digit:
# 			largest_digit = n % 10
# 		return find_largest_digit_helper(n//10, largest_digit)


if __name__ == '__main__':
	main()