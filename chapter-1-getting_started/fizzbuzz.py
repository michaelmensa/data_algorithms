#!/usr/bin/python3
'''
Sample algorithmic problem
Getting started with simple fizz buzz algorithm
'''

def fizzbuzz(num):
    ''' function that takes a list of numbers and returns
    a list of numbers.
    returns fizz in list if number is divisible by 3,
    returns buzz in list if number is divisible by 5,
    returns fizzbuzz in list if number is divisible by 3 and 5
    '''
    result = []
    for n in num:
        if n % 3 == 0 and n % 5 == 0:
            result.append('fizzbuzz')
        elif n % 3 == 0:
            result.append('fizz')
        elif n % 5 == 0:
            result.append('buzz')
        else:
            result.append(n)
    return result
