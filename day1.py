
def day1(numbersInCombination):
	file = open("day1input1.txt", "r")
	numbers=[]
	for num in file:
		num=int(num)
		if(num<2020):
			numbers.append(num)
	numbers.sort()

	import itertools
	for subset in itertools.permutations(numbers,numbersInCombination):
		print(subset)
		if sum(subset)==2020:
			import numpy
			print(subset)
			print(numpy.prod(subset))
			break
	
day1(2)
day1(3)