'''
This is a program that inherits from the node and unorderdered List Modules
Author: Marc Batete
'''
import random
from ListNode import Node
from unorderedList import UnorderedList

fp = open("processor_jobs.dat", "r")
mylist = UnorderedList()
while True:
    line = fp.readline()
    if line =="":
        break
    line = line.strip()
    word = line.split()

    value = word[0]
    mylist.add(value)
mylist.traversal()
mylist.sum()
