'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    found_starting_index = word.find('th')
    if found_starting_index == -1:
        return 0
    # is there anymore words after the th
    elif len(word[found_starting_index + 2:]) == 0:
        return 1
    else:
        return  1 + count_th(word[found_starting_index + 2:])
    