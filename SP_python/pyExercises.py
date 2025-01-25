def ggT(n, k):
    print(n, k)
    if k == 0:
        return n
    return ggT(k, n % k)


def ackermann(n, k):
    if n == 0:
        return k + 1
    elif k == 0:
        return ackermann(n - 1, 1)
    else:
        return ackermann(n - 1, ackermann(n, k - 1))


def palindrom(wort):
    # Base case 1: If the string is empty or has only one character, it's a palindrome
    if len(wort) <= 1:
        return True
    # Base case 2: If the first and last characters don't match, it's not a palindrome
    if wort[0] != wort[-1]:
        return False
    # Recursive case: Check the substring without the first and last characters
    return palindrom(wort[1:-1])


class A:
    def out(self):
        return 10


class B(A):
    def out(self):
        return 2 * super().out()


class C(A):
    def out(self):
        return 4 * super().out()


class D(B, C):
    def out(self):
        print(super().out() * 3)


# D().out()

def sum_a_b(a, b):
    summe = 0
    if a < b:
        for n in range(a, b + 1):
            summe += n
    else:
        for n in range(b, a + 1):
            summe += n
    print(summe)


def reversed_quad(li):
    quad = []
    for i in li:
        quad.append(i * i)
    return quad[::-1]


li = [1, 2, 3, 4, 5]


# print(reversed_quad(li))

def fac(n):
    factorial = 1
    if n == 0:
        return 0
    else:
        while n > 1:
            factorial *= n
            n -= 1
    return factorial


# print(fac(4))

def with_index(l):
    index = 0
    dictionary = {}
    for i in l:
        dictionary[index] = i
        index += 1
    return dictionary

l = [1,2,3,4,5,6,6]
# print(with_index(l))

def quersumme(n):
    sum= 0
    n = str(n)
    for e in n:
        sum += int(e)
    return sum

n = 123
# print(quersumme(n))

def is_prim(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def vorkommen(n):
    vorkommen_dict = {}

    n = n.lower()

    for buchstabe in n:
        if buchstabe in vorkommen_dict:
            vorkommen_dict[buchstabe] += 1
        else:
            vorkommen_dict[buchstabe] = 1

    return vorkommen_dict

def mitternacht(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return 0

    if delta == 0:
        x1 = -b / (2 * a)
        return int(x1)

    sqrt_delta = delta ** 0.5
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)

    return int(x1 + x2)

def ggT(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def kgV(a, b):
    return abs(a * b) // ggT(a, b)