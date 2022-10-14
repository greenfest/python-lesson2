import math

def getFactorials(n):
    arrFactorials = []
    for num in range(1, n + 1):
        arrFactorials.append(math.factorial(num))
    return arrFactorials;

n = int(input("Введите число N: "))
arrFactorials = getFactorials(n)
print(arrFactorials)

