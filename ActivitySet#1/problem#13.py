#program 4b
score = input("Enter Score: ")
score = float(score)
if score >=0.9 and score >= 0 and score <=1.0:
	print("A")
elif score >=0.8 and score >= 0 and score <=1.0:
	print("B")
elif score >=0.7 and score >= 0 and score <=1.0:
	print("C")
elif score >=0.6 and score >= 0 and score <=1.0:
	print("D")
else:
	print("out of range")