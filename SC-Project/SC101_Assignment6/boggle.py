"""
File: boggle.py
Name: Yi Lin Yang
----------------------------------------
This program will search through the word board input by the user,
finding all existing words on the board in the given dictionary.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program will search through the word board input by the user,
	finding all existing words on the board in the given dictionary.
	"""
	start = time.time()
	####################
	board = []
	if user_input(board):
		boggle(board)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def user_input(board):
	# user input 16 characters (creating a 4X4 board)
	for i in range(4):
		print(i + 1, end=' ')
		string = input('row of letters: ')
		board.append([])
		if len(string) != 7:
			print('Illegal input')
			return False
		else:
			for j in range(len(string)):
				if j % 2 == 0:
					if string[j].isalpha():
						board[i].append(string[j].lower())
					else:
						print('Illegal input')
						return False
				elif j % 2 == 1:
					if string[j] != ' ':
						print('Illegal input')
						return False
	return board


def boggle(board):
	dict_set = read_dictionary()
	ans_lst = []
	for i in range(len(board)):
		for j in range(len(board)):
			row = i
			col = j
			cur_s = [board[i][j]]
			path = [(i, j)]
			boggle_helper(board, dict_set, ans_lst, row, col, cur_s, path)
	print(f'There are {len(ans_lst)} words in total.')


def boggle_helper(board, d, ans_lst, row, col, cur_s, path):
	# base case
	if len(cur_s) >= 4:
		word = ''.join(cur_s)
		if word not in ans_lst:
			if word in d:
				print(f'Found "{word}"')
				ans_lst.append(word)
	if len(path) == len(board)**2:
		return

	# recursive
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			new_row = row + i
			new_col = col + j
			if 0 <= new_row < len(board):
				if 0 <= new_col < len(board):
					if (new_row, new_col) not in path and cur_s not in ans_lst:
						# choose
						path.append((row, col))
						cur_s.append(board[new_row][new_col])
						# recursive
						boggle_helper(board, d, ans_lst, new_row, new_col, cur_s, path)
						# un-choose
						path.pop()
						cur_s.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dict_set = {}
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip()
			if 4 <= len(word) <= 16:
				dict_set[word] = 0
	return dict_set


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	dict_set = read_dictionary()
	has_prefix_helper(sub_s, dict_set)


def has_prefix_helper(sub_s, dict_set):
	for word in dict_set:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
