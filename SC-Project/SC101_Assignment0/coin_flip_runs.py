"""
File: coin_flip_runs.py
Name: Yi Lin Yang
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def main():
	"""
	This function will randomly choose head (H) or tails (T),
	and recording the times showing H or T continuously.
	The function will stop once the assigned times is reached,
	and showing a string of the process.
	"""
	print("Let's flip a coin!")
	num_run = int(input("Numbers of runs: "))
	flip1 = flip_coins()
	sequence = flip1
	runs = 0
	is_in_a_row = False				# judge whether count the run yet
	while True:
		flip2 = flip_coins()
		if flip1 == flip2:
			if not is_in_a_row:
				runs += 1
				is_in_a_row = True
		else:
			is_in_a_row = False
		sequence += flip2
		flip1 = flip2
		if runs == num_run:
			break
	print(sequence)


def flip_coins():
	"""
	This function will randomly choose 0 or 1,
	and return T or H, respectively.
	:return 'T': if random number is 0
	:return 'H': if random number is 1
	"""
	num = random.randrange(0, 2)
	if num == 0:
		return 'T'
	elif num == 1:
		return 'H'


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
