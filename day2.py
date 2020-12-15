import re

regex = re.compile("(\d{1,2})-(\d{1,2}) (\w): (\w+)")
validatesCond1=0
validatesCond2=0
def conditionOne(val1,val2,ch,password):
	count = password.count(ch)
	return val1<=count<=val2
		
def conditionTwo(val1,val2,ch,password):
	return (password[val1-1]==ch) ^ (password[val2-1]==ch)

def day2():
	global validatesCond1,validatesCond2
	with open("day2input1.txt") as file:
		for data in file:
			d =re.match(regex,data)
			val1,val2,ch,password=int(d.group(1)),int(d.group(2)),d.group(3),d.group(4)
			if conditionOne(val1,val2,ch,password):
				validatesCond1+=1
			if conditionTwo(val1,val2,ch,password):
				validatesCond2+=1
	print(validatesCond1,validatesCond2)

day2()