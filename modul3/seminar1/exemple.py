# if statement

if True:
    print("Working")


var1 = int(input("give number: "))
if var1 == 10:
    print(f"Numarul este {var1}")
elif var1 >10:
    print(f"Numarul este mai mare decat {var1}")
else:
    print(f"Numarul este mai mic decat{var1}")

# AND si OR si NOT

#AND
# 0 1 = 0
# 1 0 = 0
# 1 1 = 1
# 0 0 = 0

# OR
# 0 1 = 1
# 0 0 = 0
# 1 0 = 1
# 1 1 = 1

# NOT
# 1 = 0
# 0 = 1

print("Result of a and '' is: ", "a" and '')
print("Result of a or b is: ", "a" or 'b')
print("Result of a and b is: ", "a" and 'b')
print("Result of a and [] is: ", "a" and [])

print("Result of True or False is: ", True or False)
print("Result of not True or False is: ", not True or False)


# for loop

for letter in "Hello":
    print(letter)

for number in range(100):
    print(number)

for number in range(1, 10, 2):
    print(number)


# while loop

while True:
    number = input("give number")
    print(f"Number is: {number}")


while int(input("Give number: ")) < 100:
    print("Number is to small")



str1 = "Hello"
index = 0
while True:
    letter = str1[index]
    index += 1
    if letter == 'l':
        continue
    print(letter)
    if index >= len(str1):
        break