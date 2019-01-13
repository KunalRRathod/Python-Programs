def (rightangletriangle):
	angle_1 = print ("Enter the first angle")
	angle_2 = print ("Enter the second angle")
	angle_3 = print ("Enter the third angle")

	# A Triangle is a closed figure with 3 sides
	# A Right angle triangle is a triangle having one angle of 90 degree
	# The sum of all three angles of triangle is always less than 180 degree

	# Step 1 
	# Check for sum of angles
	if (angle_1+angle_2+angle_3 <= 180):
		print("Angles belong to a triangle")

		# Step 2
		# Conditions for right angle triangle 
		# Condition 1 : Two angles of 45 degree and one of 90 degree
		# Condition 2 : One angle of 30 degree other of 60 degree and third of 90 degree

		# Check for Condition 1
	elif (angle_1 = 45 and angle_2 = 45 and angle_3 = 90):
		print("It is a right angle triangle")
	elif (angle_1 = 45 and angle_2 = 90 and angle_3 = 45):
		print("It is a right angle triangle")
	elif (angle_1 = 90 and angle_2 = 45 and angle_3 = 45):
		print("It is a right angle triangle")

		# Check for Condition 2
	elif (angle_1 = 30 and angle_2 = 60 and angle_3 = 90):
		print("It is a right angle triangle")
	elif (angle_1 = 60 and angle_2 = 90 and angle_3 = 60):
		print("It is a right angle triangle")
	elif (angle_1 = 90 and angle_2 = 60 and angle_3 = 30):
		print("It is a right angle triangle")
	else :
		print ("The angles do not belong to a right angle triangle")
		return rightangletriangle