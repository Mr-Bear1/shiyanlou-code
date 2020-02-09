for i in range(1,101):
	b=str(i)
	if i%7==0 or b[0]=='7' or b[-1]=='7':
		i+=1
		continue
	print(i)
	i+=1

