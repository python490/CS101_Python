#Define a procedure, product_list,
#takes as input a list of numbers,
#and returns a number that is
#the result of multiplying all
#those numbers together.

#product_list([9]) => 9
#product_list([1,2,3,4]) => 24

def product_list(p):
	total =1 # works for any value
	for i in p:
		total = total * i
	return total

	