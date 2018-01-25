'''
https://www.codewars.com/kata/getting-along-with-integer-partitions/python
From wikipedia https://en.wikipedia.org/wiki/Partition_(number_theory)
In number theory and combinatorics, a partition of a positive integer n,
also called an integer partition, is a way of writing n as a sum of positive
integers. Two sums that differ only in the order of their summands are
considered the same partition.

For example, 4 can be partitioned in five distinct ways:

4, 3 + 1, 2 + 2, 2 + 1 + 1, 1 + 1 + 1 + 1

We can write:

enum(4) -> [[4],[3,1],[2,2],[2,1,1],[1,1,1,1]] and

enum(5) -> [[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]].

The number of parts in a partition grows very fast. For n = 50 number
of parts is 204226, for 80 it is 15,796,476 It would be too long to tests
answers with arrays of such size. So our task is the following:

1 - n being given (n integer, 1 <= n <= 50) calculate enum(n) ie the partition
of n. We will obtain something like that:
enum(n) -> [[n],[n-1,1],[n-2,2],...,[1,1,...,1]] (order of array and sub-arrays
doesn't matter). This part is not tested.

2 - For each sub-array of enum(n) calculate its product. If n = 5 we'll obtain
after removing duplicates and sorting:

prod(5) -> [1,2,3,4,5,6]

prod(8) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 18]

If n = 40 prod(n) has a length of 2699 hence the tests will not verify such
arrays. Instead our task number 3 is:

3 - return the range, the average and the median of prod(n) in the following
form (example for n = 5):

"Range: 5 Average: 3.50 Median: 3.50"


My solution:
'''

from functools import reduce
def part(n):
    l = [[n]]   # l is going to contain our partitions. The first partition
                # is just n, so we make a list containing n and put it in l

    while l[-1][0]>1:   # <- We will know we're done when we reach the integer
                        # partition 1+1+...+1 = n. The way this algorithm
                        # works, the first entry in the each partition list is
                        # going to be the largest number.
        l2 = l[-1][:]   # <- We make a copy of the last partition list
        for i in range(len(l2)-1,-1,-1):    # <- for each index in the partition
                                            # list going backwards
            if (all([j==1 for j in l2[i+1:]]) and l2[i]>1): # <- We check to see
                                    # if each item in the list beyond the current
                                    # index we're considering is equal to one
                                    # AND the item is greater than one, we proceed
                x = l2[i] - 1 # We subtract 1 from this entry...
                b = sum(l2[:i]) # Take the sum of the partition list to that point...
                l2 = l2[:i] + [x for i in range((n-b)//x)] # and then we set l2 equal
                                            # to the partition list up to that point,
                                            # and then repeat 'x' as many times as
                                            # we can while not causing the sum of the
                                            # list to exceed the value of n.
                                            # so:
                                            # n = 7
                                            # l[-1] = [4,1,1,1]
                                            # the new partition is [3,3,1]
                if (n-b)%x != 0: l2.append((n-b)%x) # <- we tack on anything that is left
                                                    # over
                l.append(l2) # <- and then append this to the end of l!
    l = sorted(list({reduce(lambda x, y: x * y, i, 1) for i in l}))
    r = max(l)-min(l)
    a = sum(l) / float(len(l)) # for Python 2 compatibility
    m = (l[len(l)//2] + l[(len(l)-1)//2])/2.0
    return("Range: {0} Average: {1:.2f} Median: {2:.2f}".format(r,a,m))
