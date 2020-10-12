'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

time complexity is Big O of N
'''
def count_th(word):
    #base case return 0
    if len(word) < 2: 
        return 0
    #check if first two letters of current word are th
    if word[:2] == 'th':
        #if th is found add 1 and run recursion after 'th'
        return 1 + count_th(word[2:])
    else:
        #if th is not in front of word drop first letter and run recursion
        return count_th(word[1:])
