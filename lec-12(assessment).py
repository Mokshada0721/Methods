# filter method()
# eg: 1
''' num = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, num) #lambda function checks if a number is
                                        # even and filter is applied to the cond
print(list(even))         # O/P: [2,4] '''

# eg: 2
'''ages = [10, 12, 13, 16, 18, 20, 25, 21]
adults = filter(lambda age: age >= 18, ages)   # Function to filter adults using filter with lambda
print(list(adults))        # O/P: [18, 20, 21, 25]'''

# eg: 3
'''inp_list = ['s', 'h', 'o', 'e', 's']
result = list(filter(lambda x: x!='e', inp_list))  
print(list(result))'''    # ['s', 'h', 'o', 's']

# map method ()
# eg 1: double each num
'''a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))'''

# eg 2: converting fahrenheit to celsius
'''num = [32, 68, 100, 212]
result = map(lambda x: (x-32)*5/9, num)
print(list(result))'''

#eg 3:
fruits = ["apple", "banana", "cherry"]