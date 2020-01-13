'''
This is a short application of the use of the node class
Author: Marc Batete
'''
import random
from ListNode import Node
from unorderedList import UnorderedList

mylist = UnorderedList()

#value = raw_input(" enter a number: ")

while True:
    value = raw_input(" enter a number: ")
   
    if value == "":
        break
    else:
     mylist.add(value)

mylist.traversal()
