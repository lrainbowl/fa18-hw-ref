import numpy as np

"""
matrix_multiply

Given two 2-D input arrays `arr0`, `arr1`, return the matrix product arr0 * arr1.
Return None if the matrix product does not exist.

As with math, assume that indices are in [row][column] format, so each inner list is a row.
"""
def matrix_multiply(arr0, arr1):
    if not arr0 or not arr1 or len(arr0[0]) != len(arr1):
        return None
    return np.matmul(arr0, arr1)
            

"""
nth_largest_element

Given an input list `arr`, and index `n`, return the nth largest element.
Avoid using built-in sorting methods.
"""
def nth_largest_element(arr, n):
    if not arr or n > len(arr) or n < 1:
        return None
    if (n == 1):
        return max(arr)
    else:
        largest = max(arr)
        return(nth_largest_element([num for num in arr if num != largest], n-1))

"""
reverse_block

Given an input list `arr`, and a block size `n` > 0, reverse the list in blocks of n.

Example:
	Arguments:
		[1,2,3, 4,5,6, 7], 3
	Return:
		[3,2,1, 6,5,4, 7]
	(spacing added for emphasis)

"""
def reverse_block(arr, n):
    if not arr or n > len(arr) or n <= 0:
        return None
    result = []
    i = 0
    while i < len(arr):
        block = []
        while len(block) < n and i < len(arr):
            block.append(arr[i])
            i += 1
        block.reverse()
        result.extend(block)
    return result

"""
subset_sum

Given an input list `arr`, and a number `target`, return whether or not any possible subset of the values in `arr` could sum to `target`.

Example 1:
	Arguments:
		[1,2,3,4,5,7], 13
		7 + 4 + 2 = 13
	Return:
		True

Example 2:
	Arguments:
		[1,2,-1,5,4,-196], 196
	Return:
		False
"""
def subset_sum(arr, target):
    if not arr:
        return False
    arr.sort(reverse=True)
    if arr[0] == target:
        return True
    return subset_sum(arr[1:], target - arr[0]) or subset_sum(arr[1:], target)

"""
spiral_matrix

Given an input 2-D array, return a list with the values obtained by following a clockwise spiral path, starting from [0][0], then proceeding to [0][n], [m][n], [m][0], then going inwards:

Example:
	Argument:
		[[a,b,c,d,e],
		 [f,g,h,i,j],
		 [k,l,m,n,o],
		 [p,q,r,s,t],
		 [u,v,w,x,y]]
	Return:
		[a,b,c,d,e, j,o,t,y, x,w,v,u, p,k,f, g,h,i, n,s, r,q, l, m]
"""
def spiral_matrix(arr):
    if not arr:
        return None
    arr = np.array(arr)
    spiral = []
    while arr.size:
        spiral.append(arr[0])
        arr = arr[1:].T[::-1]
    return np.concatenate(spiral)
