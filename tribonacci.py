def tribonacci(n: int) -> int:
    if n==0 or n==1:
        return 1
    elif n == 2:
        return 2
    return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
# Verejne testy
print(tribonacci(0))  # 1
print(tribonacci(1))  # 1
print(tribonacci(2))  # 2
print(tribonacci(3))  # 4
print(tribonacci(4))  # 7
print(tribonacci(5))  # 13
print(tribonacci(6))  # 24
print(tribonacci(7))  # 44