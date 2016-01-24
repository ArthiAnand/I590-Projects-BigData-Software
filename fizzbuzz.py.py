# -*- coding: utf-8 -*-
#Write a python program called fizzbuzz.py that accepts an integer n from the command line.
#Pass this integer to a function called fizzbuzz. The fizzbuzz function should then iterate from 1 to n.
#If the ith number is a multiple of two, print “fizz”, if a multiple of three print “buzz”, 
#if a multiple of both print “fizzbuzz”, else print the value.

n = raw_input("Enter an integer:  ") 
n = int(n)

def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 6 == 0:
            print "fizzbuzz"
        elif i % 3 == 0:
            print "buzz"
        elif i % 2 == 0:
            print "fizz"
        else:
            print i

fizzbuzz(n)