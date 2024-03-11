num = int(input('Enter the number : '))

#binary representation
bit_to_string = str(bin(num))
bit = bit_to_string[2:]
print('Binary representation of {} is {}'.format(num,bit))

#total number of bits in binary representation
print('Number of bit in {} is {}'.format(num, num.bit_length()))

#total number of 1's in binary representation
print('Number of 1\'s in binary representation of {} is {}'.format(num, num.bit_count()))

#total number of 0's in binary representation
print('Number of 0\'s in binary representation of {} is {}'.format(num, num.bit_length() - num.bit_count()))
