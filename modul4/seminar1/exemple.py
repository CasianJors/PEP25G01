
# functions

def message():
    print("Enter a value: ")

print("We start here.")
message()
print("We end here.")



var1 = 1

def sum_numbers(number_a, number_b):
    global var1
    var1 = var1 + 1
    result = number_a + number_b + var1
    return result

result1 = sum_numbers(10, 20)
result2 = sum_numbers(10, 20)
result3 = sum_numbers(10, 20)
print(result3)
print(var1)



