# exceptions
# print(11/int(input("Divider:")))

try:
    if True:
        print(11/int(input("Divider:")))
    else:
        pass
except ZeroDivisionError:
    print("Divider should not be 0")
except ValueError:
    print("Not a number")
except Exception:
    print("Some other error happened")
else:
    print("Success")
finally:
    print("All Done")


# recursivitate
# factorialn = 1*2*3*4*5 = 5!

def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial1(5))


def factorial2(n):
    if n == 1:
        return 1
    return factorial2(n - 1)

# prima apelare       factorial2(4) * 5   => factorial(3) * 4 * 5 => factorial(2) * 3 * 4 * 5 => factorial(1) * 2 * 3 * 4 * 5 => 1 * 2 * 3 * 4 * 5

#a doua apelare       factorial(3) * 4 => factorial(2) * 3 * 4 => factorial(1) * 2 * 3 * 4 => 1* 2 * 3 * 4

#a treia apelare      factorial(2) * 3 => factorial(1) * 2 * 3 => 1 * 2 * 3

# a patra apelare     factorial(1) * 2 => 1*2

#a cincia apelare     1

print(factorial2(5))