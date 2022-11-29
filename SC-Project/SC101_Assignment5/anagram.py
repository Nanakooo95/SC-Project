"""
File: anagram.py
Name: Yi Lin Yang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program will search and print all anagrams of the given string
    from the dictionary text file.
    """
    start = time.time()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(s)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        dict_lst = []
        for line in f:
            dict_lst.append(line.strip())
    return dict_lst


def find_anagrams(s):
    """
    :param s: the given string
    :return: None
    """
    s_lst = []
    anagram_lst = []
    index_lst = []
    dict_lst = read_dictionary()
    for i in range(len(s)):
        s_lst.append(s[i])
    find_anagrams_helper(s_lst, [], anagram_lst, dict_lst, index_lst)
    print(len(anagram_lst), 'anagrams:', anagram_lst)


def find_anagrams_helper(s_lst, current_lst, anagram_lst, dict_lst, index_lst):
    anagram = ''
    for i in range(len(current_lst)):
        anagram += current_lst[i]
    if len(current_lst) == len(s_lst):
        for word in dict_lst:
            if word == anagram and word not in anagram_lst:
                print('Found:', word)
                print('Searching...')
                anagram_lst.append(word)
                return
    else:
        for i in range(len(s_lst)):
            if i not in index_lst:
                # choose
                current_lst.append(s_lst[i])
                index_lst.append(i)

                if has_prefix(anagram):
                    # explore
                    find_anagrams_helper(s_lst, current_lst, anagram_lst, dict_lst, index_lst)
                    # un-choose
                current_lst.pop()
                index_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: the sub string which has been re-combined
    :return: helper function
    """
    dict_lst = read_dictionary()
    return has_prefix_helper(sub_s, dict_lst)


def has_prefix_helper(sub_s, dict_lst):
    for word in dict_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
