

def day3(verticalPas,OrizontalPas):
	maptree=[]
	countTreesOnPath=0
	with open("day3input.txt") as file:
		for data in file:
			maptree.append(str(data))

	vertical=0
	orizontal=0
	lineSize=len(maptree[0])-1
	while vertical!=len(maptree)-1:
		vertical+=verticalPas
		orizontal+=OrizontalPas
		if orizontal>=lineSize:
			orizontal-=lineSize
		
		if maptree[vertical][orizontal]=='#':
			countTreesOnPath+=1
	return countTreesOnPath

pasList=[(1,1),(1,3),(1,5),(1,7),(2,1)]

ans=[]
for v,o in pasList:
	ans.append(day3(v,o))
	
import numpy
print(numpy.prod(ans))
