'''
https://www.codewars.com/kata/recover-a-secret-string-from-random-triplets/python

There is a secret string which is unknown to you. Given a collection of random
triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter
occurs somewhere before the next in the given string. "whi" is a triplet for
the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the
secret string.

You can assume nothing about the triplets given to you other than that they are
valid triplets and that they contain sufficient information to deduce the
original string. In particular, this means that the secret string will never
contain letters that do not occur in one of the triplets given to you.

My solution:
'''
def recoverSecret(triplets):
    # I feel like this is quick and dirty, and I'm sure there's a
    # more clever way to go about it - but here it is:
    # This creates a list of the unique letters in the triplets
    letters = list(set(''.join([''.join(i) for i in triplets])))
    counter = 0
    while True:
        # This checks to see if we've gone through all of our triplets
        # without modifying our list of letters. If so, returns.
        if counter >= len(triplets):
            return ''.join(letters)
        for i in triplets:
            # This puts the index where each letter in the triplet we're
            # looking at appears in our list.
            a = [letters.index(j) for j in i]
            # If they're all in the right order, we're good!
            # Add one to the counter so we know we haven't modified the list.
            if a[0] < a[1] < a[2]:
                counter += 1
            else:
                # If they aren't in the right order, we take the list of indices
                # and sort it. Then we assign each letter in the triplet to a
                # position in the list - such that the letter that appears first
                # is assigned to the spot in the list with the lowest index, and so on.
                a = sorted(a)
                counter = 0
                for v,j in enumerate(i):
                    letters[a[v]] = j
