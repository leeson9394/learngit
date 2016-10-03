input_num=input("Enter an integer: ")
bin_input=[int(i) for i in str(bin(input_num))[2:]]

bin_input.reverse()
bin_output=int(''.join(map(str,bin_input)),2)

print "Output integer: ",bin_output