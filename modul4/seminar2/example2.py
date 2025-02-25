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

def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial1(5))


def factorial2(n):
    if n == 1:
        return 1
    return factorial2(n - 1) * n


print(factorial2(995))