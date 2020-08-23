import geocoder as gc
def isPresent():
	#geocoder should be imported as gc

	#arbitrary coordinates
	class_lat=[100,120,140,118]
	class_lng=[120,100,120,140]

	#getting location of student using geocoder
	student_location= gc.ip('me')
	std_lat=student_location.latlng[0]#latitude
	std_lng= student_location.latlng[1]#longitude

	#test condition when condition is true
	std_lat=110
	std_lng=120


	#print(std_lat, std_lng)

	#conditionals to check presence of student

	lat=0
	lng=0
	if std_lat>=min(class_lat) and std_lat<=max(class_lat):
	    lat=1
	if std_lng>=min(class_lat) and std_lat<=max(class_lat):
	   lng=1
	   

	#producing output(will be converted to function return value)
	if lat==1 and lng==1:
	    print("true")
	else:
	    print("false")

