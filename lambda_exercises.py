''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers_list)

evens_list = list(filter(lambda x: x % 2 == 0, numbers_list))
print(evens_list)

odds_list = list(filter(lambda x: x % 2, numbers_list))
print(odds_list)



''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


wkdays_of_six = list(filter(lambda day: len(day) == 6, weekdays))
print(wkdays_of_six)






''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
Original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
Remove_words =['orange', 'black']
new_list = list(filter(lambda word: word not in Remove_words, Original_list))
print(new_list)








''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 =[2, 4, 6, 8]
list3 = list(filter(lambda word: word not in list2, list1))
print(list3)




''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''

Original_list = ['red', 'black', 'white', 'green', 'orange']
search_string = ['ack']
list5 = list(filter(lambda x: search_string in x, Original_list))




''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world"
str1 = "HELLO"
str1= "hello"

password_list = ['Hello8world','HELLO','hello']

for password in password_list:
    upper = any(map(lambda x: x.isupper(),password))
    lower = any(map(lambda x: x.islower(),password))
    digit = any(map(lambda x: x.isdigit(),password))
    length = len(password) >= 8

criteria = upper and lower and length and digit

print({password},{criteria})

#WHY DONT U WORK??











''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

original_scores.sort(key=lambda num: num[1])
print(original_scores)
