remainder = lambda num: num % 2

print(type(remainder))
print(remainder(5))

product = lambda x,y: x * y

print(product(2,3))



def testfunc(num):
    return lambda x: x * num

result10 = testfunc(10)
result100 = testfunc(100)

print(result10(9))
print(result100(9))

#This is the exact same thing as above just without calling the function ltr
result10 = lambda x: x * 10
result100 = lambda x: x * 100




numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

filtered_list = list(filter(lambda x: (x>7), numbers_list))# In order to actually SEE the new list, 
#you have to wrap the code in a list function

print(filtered_list)



mapped_list = list(map(lambda x: x % 2, numbers_list))
print(mapped_list)
