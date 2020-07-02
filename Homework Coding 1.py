# Find the smallest number from a list of numbers given below :
# 18,35,12,45,-4,14,88,11,13,1


arithmetic_list = [18,35,12,45,-4,14,88,11,13,1]
temp_variable = arithmetic_list[0]
for atharva_variable in arithmetic_list[1:] :
	if(atharva_variable < temp_variable):
		temp_variable = atharva_variable
print("The Smallest Number is : "+  str(temp_variable))