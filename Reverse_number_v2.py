import sys	

input_num=input("Enter an integer N that 1 <= N <= 1000000000: ")
if 1 <= input_num <= 1000000000
	bin_input=[int(i) for i in str(bin(input_num))[2:]]
	bin_input.reverse()
	bin_output=int(''.join(map(str,bin_input)),2)

	print "Output integer: ",bin_output
else:
	print "Input number not in range"