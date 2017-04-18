# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# ���ۃN���X
class CalcNode(metaclass=ABCMeta):
	@abstractmethod
	def className(self):
		pass
	
	@abstractmethod
	def calc(self):
		pass

#���ۃN���X�̒��g�BZero,Add,Sub��3�̃N���X
class classZero(CalcNode):
	def __init__(self):
		self.name = "Zero"
	
	def className(self):
		return self.name
	
	def calc(self,val1=1,val2=2):
		return 0

class classAdd(CalcNode):
	def __init__(self):
		self.name= "Add"
	
	def className(self):
		return self.name
	
	def calc(self,val1=1,val2=2):
		return val1+val2

class classSub(CalcNode):
	def __init__(self):
		self.name= "Sub"
	
	def className(self):
		return self.name
	
	def calc(self,val1=1,val2=2):
		return val1-val2

def factory(className):
	if className=="Zero":
		return classZero()
	elif className=="Add":
		return classAdd()
	elif className=="Sub":
		return classSub()
	else:
		raise

def main():
	nodes=(factory("Add"),
			factory("Zero"),
			factory("Sub"))
	
	for node in nodes:
		print(node.className())
		print(node.calc(val1=2,val2=5))
		print(node.calc(val2=5,val1=2)) #����ւ��Ă����v
		print(node.calc(2,5))           #�ϐ������Ȃ��Ă����v
		print(node.calc(val1=100))      #�Е���������Ă����v
		print(node.calc(val2=100))      #�Е���������Ă����v
		print(node.calc())              #��������Ȃ��Ă����v

#main()�����s����
if __name__== '__main__':
    main()
