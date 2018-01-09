#from math import ceil, floor

x = float(input("Vstavi temperaturo:"))
if -0.5 <= x < 0:
	print ("-0")

else:
	decimalni_del = x - floor(x)
	if decimalni_del >= 0.5:
		print (ceil(x))

	else:
		print(round(x))
