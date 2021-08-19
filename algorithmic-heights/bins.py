"""
Binary search is the ultimate divide-and-conquer algorithm. To find a key k in a large file containing keys A[
1..n] in sorted order, we first compare k with A[n/2], and depending on the result we recurse either on the first
half of the file, A[1..n/2], or on the second half, A[n/2+1..n]. The recurrence now is T(n)=T(n/2)+O(1). Plugging
into the master theorem (with a=1,b=2,d=0) we get the familiar solution: a running time of just O(logn).
"""


def bins(array, start, end, number):
    # Base case
    if start > end:
        return -1

    middle = (start + end) // 2
    if array[middle] == number:
        return middle
    elif array[middle] < number:
        return bins(array, middle + 1, end, number)
    else:
        return bins(array, start, middle - 1, number)


with open("rosalind_bins.txt", "r") as f:
    n = int(f.readline())
    m = int(f.readline())
    a = f.readline().split()
    a = tuple(int(i) for i in a)
    m_arr = f.readline().split()


with open("rosalind_bins_output.txt", "w") as ff:
    for k in map(int, m_arr):
        result = bins(a, 0, len(a) - 1, k)
        # The problem specifies one-based indexing, so we add +1 to the result
        if result == -1:
            print(-1, end=" ", file=ff)
        else:
            print(result + 1, end=" ", file=ff)
