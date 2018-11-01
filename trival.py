l=[]
for i in range(0,3):
	l.append(int(input()))
		
if(l[0]+l[1]>l[2]):
	if(l[0]+l[2]>l[1]):
		if(l[1]+l[2]>l[0]):
			print("triangle is valid")
else:
	print ("The triangle not valid")
	


