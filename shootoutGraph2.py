def ccw(a,b,c):
	return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
t=input()
while t:
	t-=1
	a=map(int,raw_input().split())
	c=map(int,raw_input().split())
	b=map(int,raw_input().split())
	d=map(int,raw_input().split())
	if(ccw(a,b,c)*ccw(a,b,d)<0 and ccw(c,d,a)*ccw(c,d,b)<0): #Intersection exists and is proper between AB and CD
		print "No"
	else:
		print "Yes"