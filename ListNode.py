'''
This is a module implementing a Node Class.
Author: Marc Batete
'''
class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,data):
		self.data = data

	def setNext(self,pnext):
		self.next = pnext



	
	
