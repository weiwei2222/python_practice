# recursion 递归练习

def count_sum(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return n + count_sum(n-1)


abc = count_sum(100)
print(abc)


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\nRecursion Example Results")
abcd = tri_recursion(6)