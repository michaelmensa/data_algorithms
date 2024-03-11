#!/usr/bin/python3

check_duplicates = __import__('check_duplicates').check_duplicates

print(check_duplicates([1, 2, 3, 4, 3, 5, 4, 2, 1, 6, 7, 8]))

print(check_duplicates([5, 6, 7, 3, 2]))
