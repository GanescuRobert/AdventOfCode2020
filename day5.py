



def move(ch,FB,LR):
	
	if ch == 'B':
		FB = FB[int(len(FB)/2):]
	if ch == 'F':
		FB = FB[:int(len(FB)/2)]
	if ch == 'R':
		LR = LR[int(len(LR)/2):]
	if ch == 'L':
		LR = LR[:int(len(LR)/2)]
	return FB,LR
def findSeat(seats):
	for i in range(2,len(seats)):
		if seats[i-1]+1!=seats[i]:
			print(seats[i-1]+1)
			return


def day5():
	maxx=0
	seats=[]
	with open("day5input.txt",'r') as file:
		for data in file:
			FB=[*range(0,128)]
			LR=[*range(0,8)]
			for ch in data:
				FB, LR = move(ch,FB,LR)
			
			ans=FB[0]*8+LR[0]
			seats.append(ans)
			if maxx < ans:
				maxx=ans
	print(maxx)
	seats.sort()
	findSeat(seats)


day5()
