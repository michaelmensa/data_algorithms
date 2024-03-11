#!/usr/bin/python3

'''
function to check duplicates
'''


def check_duplicates(num):
    ''' function to check duplicate numbers in list of numbers
    '''
    duplicates = []
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] == num[j] and num[i] not in duplicates:
                duplicates.append(num[i])
    if duplicates:
        return duplicates
    else:
        return 'no duplicates found'
