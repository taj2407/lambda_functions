########################  LAMBDA FUNCTION  #############################


#it is a anonymous single line function.lambda keyword is used for creating lambda function.
#we can use multiple arguments but we can define only single statement in lambda function.
#we can use lambda functions multiple times but only in single place.we can only perform if and else on it.
#syntax -- lambda arguments:experssions.

#ex 1 Add two number using lambda

"""res = lambda a,b: a+b
print(res(10,20))"""

#ex 2 Palindrome or not

"""palindrome = lambda s: f'Palindrome' if s == s[::-1] else f'Not a Palindrome'
print(palindrome('mam'))"""

#ex 3 Using lambda in a comprehension 

"""l = [1,2,3,4,5,6,7,8,9,10] #if it is even square the number else print the number
even = lambda i: i**2 if i % 2 == 0 else i
res = [even(i) for i in l]
print(res)"""

###map()
#it is used when we want to apply single line function.
#map function is used to apply this function to each element of the numbers list.
#map is often faster than loops.map function is a more memory-efficient.
#map function return map object,so we need to convert it using list(),tuple() etc.
#syntax -- map(function address,iterable)

#ex 1 Find the squares of all the elements in different lists using map
'''l=[1,2,3,4,5]
print(list(map(lambda x:x*2,l)))#output=[2, 4, 6, 8, 10]'''

#ex 2 Element to the power of their index
'''l=[1,2,3,4,5]
print(list(map(lambda x:x[1]**x[0],enumerate(l))))#output=[1, 2, 9, 64, 625]'''

#ex 3 Converting negative numbers into positive
#method1
'''l=[2,-3,1,-5,-8,-6]
print(list(map(abs,l)))'''
#method2
'''l=[2,-3,1,-5,-8,-6]
print(list(map(lambda x:x if x>=0 else -x,l)))'''

###fiter
#filter function filter the given sequences with the help of a function that tests to each element in the sequence to be true or not.

#ex 1 Filter the even numbers from a list
'''l=[11,22,33,44,55]
print(list(filter(lambda x:x%2==0,l)))'''

#ex 2 Filter the palindrome numbers from the list
'''l=[11,20,141,15,505,1403,1441]
print(list(filter(lambda x:str(x)[ : :-1]==str(x),l)))'''

#ex 3 Filter the nested lists based on their internal sum and length

'''l = [[1, 2, 3], [4, 5, 6, 7], [10, 1], [6, 2, 3], [3, 4, 5, 6]]
print(list(filter(lambda i: sum(i) > 10 and len(i) >= 3,l)))'''

#ex 4 Filter the words which are palindrome and have more than 3 vowels in it

'''l = ["deified", "civic", "level", "rotor", "racecar", "banana", "adieu", "education"]
print(list(filter(lambda i: i == i[::-1] and sum(1 for j in i if j in 'aeiou') > 3,l)))'''

###reduce
#it is used to operator like sum,mul and min.
#it is available in functools module.
#it takes two arguments.
#syntax:functool.reduce(function,iterable)

#finding the max number in a given list.

from functools import reduce
'''l=[11,22,33,44,55]
print(reduce(lambda a,b:a if a>b else b,l))'''

#finding the sum of numbers of given list.
'''l=[11,22,33,44,55]
print(reduce(lambda a,b:a+b,l))'''

#flattening list of nested list by using.
'''l=[[11,22],[33,44],[55]]
print(reduce(lambda a,b:a+b,l))'''

#finding lenthiest string from given list of strings.
l=['amrin','mom','misbaanjum','gubibanda sha']
print(reduce(lambda a,b:a if len(a)>len(b) else b,l))



