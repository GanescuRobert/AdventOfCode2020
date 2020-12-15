
valid_passports=0

def byr_valid(value):
	val = int(value)
	return (len(value)==4) and (1920<=val<=2002)
def iyr_valid(value):
	val = int(value)
	return (len(value)==4) and (2010<=val<=2020)
def eyr_valid(value):
	val = int(value)
	return (len(value)==4) and (2020<=val<=2030)
def hgt_valid(value):
	val=0
	val_t=""
	for ch in value:
		if ch.isdigit():
			val = val*10 + int(ch)
		else:
			val_t+=ch
	if val_t=='cm':
		return 150<=val<=193
	if val_t=='in':
		return 59<=val<=76
def hcl_valid(value):
	digits = '0123456789'
	chars = 'abcdef'
	
	val = value[1:]
	for ch in val:
		if ch not in (chars + digits):
			return False
	return value[0]=='#'
def ecl_valid(value):
	eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	return value in eye_color
def pid_valid(value): return len(value)==9 and value.isdigit()

def valid(mapMatch):
	return \
	byr_valid(mapMatch['byr']) and \
	iyr_valid(mapMatch['iyr']) and \
	eyr_valid(mapMatch['eyr']) and \
	hgt_valid(mapMatch['hgt']) and \
	hcl_valid(mapMatch['hcl']) and \
	ecl_valid(mapMatch['ecl']) and \
	pid_valid(mapMatch['pid'])

def validation(match):
	mapMatch={}
	global valid_passports
	for item in match:
		mapMatch[item[0]]=item[1]
	if len(match)==7:
		if 'cid' in mapMatch:
			return
	if valid(mapMatch):
		valid_passports+=1

def preprocess():
	output=[]
	with open("day4input.txt") as file:
		person_data=""
		for data in file:
			if data != '\n':
				data = data.replace('\n',' ')
				person_data = person_data + data
			else:
				output.append(person_data)		
				person_data=""
	
	with open("day4input.txt","w") as file:
		for item in output:
			file.write(item)
			file.write('\n')

def day4():
	import re
	preprocess()
	global valid_passports
	reg = r"\b(.+?):(.+?)\b "
	match=[]
	with open("day4input.txt",'r') as file:
		for data in file:
			match=re.findall(reg,data)
			if len(match)>=7:
				validation(match)
	print(valid_passports)

day4()

