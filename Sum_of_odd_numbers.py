
"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""

# Solution 1
def row_sum_odd_numbers(n):
    return n**3

# Solution 2 // Brute Force
def row_sum_odd_numbers(n):
    
    prime_list = []
    empty = []
    pyramid_list = ['']
    
    for i in range(n*(n+1)):
        if i % 2 != 0:
            prime_list.append(i)
    
    i = j = 0
    for x in range(len(prime_list)):
        j += 1
        if prime_list[i:i+j] != empty:
            pyramid_list.append(prime_list[i:i+j])
            i = i + j
    
    
    return sum(pyramid_list[n])
