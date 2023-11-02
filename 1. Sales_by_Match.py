
''' There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example


There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock
Returns

int: the number of pairs
Input Format

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers, , the colors of the socks in the pile.

Constraints

 where 
Sample Input

STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
Sample Output

3
Explanation



There are three pairs of socks.'''


def sockMerchant(n, ar):
    # Create a dictionary to store the frequency of each color
    color_freq = {}
    for color in ar:
        if color in color_freq:
            color_freq[color] += 1
        else:
            color_freq[color] = 1

    # Count the number of pairs for each color
    pairs = 0
    for color in color_freq:
        pairs += color_freq[color] // 2

    return pairs
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))  # Output: 3
