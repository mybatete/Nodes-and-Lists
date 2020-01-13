'''
This is a program that Classifies Processor Jobs.
Description: This programs takes a list of CPU instructions and classifies them according to their lengths.
Author: Marc Batete
'''
import random
from ListNode import Node
from unorderedList import UnorderedList

fp = open("processor_jobs.dat", "r")
short_jobs = UnorderedList()
medium_jobs = UnorderedList()
long_jobs = UnorderedList()
while True:
    line = fp.readline()
    if line =="":
        break
    line = line.strip()
    word = line.split()

    value = word[0]
    if value < 200:
        short_jobs.add(value)
    elif value > 200 and value < 1000:
        medium_jobs.add(value)
    else:
        long_jobs.add(value)
short_jobs.traversal()
medium_jobs.traversal()
long_jobs.traversal()

