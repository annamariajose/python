l= []
def funtriangle(a,b,c):
	if([a]+[b]>[c]):
		if([a]+[c]>[b]):
			if([b]+[c]>[a]):
				print("triangle is valid")
	else:
			print("triangle is not valid")

funtriangle(l[0],l[1],l[2])
